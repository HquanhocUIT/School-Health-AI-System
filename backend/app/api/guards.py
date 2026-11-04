"""Reusable authentication and role guards."""

from collections.abc import Callable
from dataclasses import dataclass

from fastapi import Depends, HTTPException, status


@dataclass(frozen=True)
class AuthenticatedUser:
    """Thông tin tối thiểu cần có từ hệ thống đăng nhập."""

    id: str
    role: str


def get_current_user() -> AuthenticatedUser:
    """
    Điểm kết nối với SCRUM-32.

    Hiện tại luôn từ chối vì hệ thống login chưa được tích hợp.
    Khi login hoàn thành, thay bằng dependency xác thực thật của nhóm.
    """
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Authentication is not available yet",
    )


def require_role(*allowed_roles: str) -> Callable:
    """Chỉ cho phép user đã xác thực có role nằm trong danh sách."""

    def role_guard(
        current_user: AuthenticatedUser = Depends(get_current_user),
    ) -> AuthenticatedUser:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource",
            )

        return current_user

    return role_guard