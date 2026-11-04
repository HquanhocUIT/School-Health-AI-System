export type UserRole = 'admin' | 'nurse' | 'parent'

export type AuthenticatedUser = {
  id: string
  email: string
  role: UserRole
}

type LoginResponse = {
  access_token: string
  token_type: 'bearer'
  expires_in: number
  user: AuthenticatedUser
}

export type LoginCredentials = {
  email: string
  password: string
}

export class AuthError extends Error {
  constructor(message: string) {
    super(message)
    this.name = 'AuthError'
  }
}

export const roleLandingPaths: Record<UserRole, string> = {
  admin: '/admin',
  nurse: '/nurse',
  parent: '/parent',
}

const api = (import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000').replace(/\/$/, '')
const sessionKey = 'schoolhealth.auth-session'

function isUserRole(value: unknown): value is UserRole {
  return value === 'admin' || value === 'nurse' || value === 'parent'
}

function isLoginResponse(value: unknown): value is LoginResponse {
  if (!value || typeof value !== 'object') return false
  const response = value as Partial<LoginResponse>
  return (
    typeof response.access_token === 'string' &&
    response.token_type === 'bearer' &&
    typeof response.expires_in === 'number' &&
    Boolean(response.user) &&
    typeof response.user?.id === 'string' &&
    typeof response.user.email === 'string' &&
    isUserRole(response.user.role)
  )
}

export async function signIn(credentials: LoginCredentials): Promise<AuthenticatedUser> {
  sessionStorage.removeItem(sessionKey)

  let response: Response
  try {
    response = await fetch(`${api}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credentials),
    })
  } catch {
    throw new AuthError('Cannot connect to the SchoolHealth sign-in service. Please try again.')
  }

  if (response.status === 401) {
    throw new AuthError('Email or password is incorrect. Please try again.')
  }
  if (response.status === 503) {
    throw new AuthError('The sign-in service is not configured yet. Please contact the project team.')
  }
  if (!response.ok) {
    throw new AuthError('Unable to sign in right now. Please try again later.')
  }

  let result: unknown
  try {
    result = await response.json()
  } catch {
    throw new AuthError('The sign-in service returned an invalid response.')
  }

  if (!isLoginResponse(result)) {
    throw new AuthError('The sign-in service returned an invalid response.')
  }

  sessionStorage.setItem(
    sessionKey,
    JSON.stringify({
      accessToken: result.access_token,
      user: result.user,
      expiresAt: Date.now() + result.expires_in * 1000,
    }),
  )
  return result.user
}

export function signOut(): void {
  sessionStorage.removeItem(sessionKey)
}
