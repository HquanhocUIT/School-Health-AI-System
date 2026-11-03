# SchoolHealth AI System

Hệ thống quản lý sức khỏe học đường, giúp nhà trường và gia đình lưu trữ hồ sơ sức khỏe học sinh, theo dõi kết quả khám định kỳ và phối hợp chăm sóc liên tục.

> Dự án đang trong quá trình phát triển. Các chức năng và công nghệ bên dưới dựa trên project brief; hướng dẫn chạy sẽ được cập nhật khi mã nguồn được thêm vào repository.

## Mục tiêu

- Tập trung hồ sơ sức khỏe và lịch sử khám của học sinh qua các năm học.
- Hỗ trợ nhập hồ sơ hiện có từ Excel, kiểm tra dữ liệu và phát hiện bản ghi trùng.
- Theo dõi kết quả khám, xu hướng sức khỏe và các trường hợp cần được chú ý.
- Giúp nhân viên y tế trường học, phụ huynh và học sinh phối hợp dựa trên quyền truy cập phù hợp.
- Đưa ra giải thích sức khỏe và gợi ý dinh dưỡng bằng AI; quyết định chuyên môn thuộc về nhân viên y tế.

## Nhóm chức năng dự kiến

1. Đăng nhập, phân quyền theo vai trò và liên kết tài khoản phụ huynh – học sinh.
2. Hồ sơ học sinh, tiền sử sức khỏe và thói quen dinh dưỡng.
3. Nhập và chuyển đổi dữ liệu Excel, có ánh xạ cột, kiểm tra và xem trước trước khi xác nhận.
4. Quản lý đợt khám, kết quả khám và ghi chú theo dõi.
5. Dashboard và báo cáo theo học sinh, lớp, năm học và đợt khám.
6. Hỗ trợ giải thích sức khỏe và gợi ý dinh dưỡng bằng Ollama.

## Công nghệ dự kiến

| Thành phần | Công nghệ |
| --- | --- |
| Frontend | React, TypeScript, Tailwind CSS |
| Biểu đồ | Recharts |
| Backend API | Python, FastAPI |
| Cơ sở dữ liệu | PostgreSQL |
| Nhập Excel | pandas, openpyxl |
| AI | Ollama |
| Kiểm thử | pytest, Playwright |
| Môi trường phát triển/demo | Docker Compose |
| Quản lý mã nguồn | Git, GitHub |

## Cấu trúc mã nguồn dự kiến

```text
.
├── frontend/                 # React + TypeScript
├── backend/                  # FastAPI
│   └── tests/                # pytest
├── frontend/tests/           # Playwright; cấu hình tại frontend/playwright.config.*
└── .github/workflows/ci.yml  # CI cho kiểm tra và kiểm thử
```

## Bắt đầu

Clone repository:

```bash
git clone https://github.com/Phuthanh123456/School-Health-AI-System.git
cd School-Health-AI-System
```

Các bước cài đặt và chạy frontend/backend sẽ được bổ sung khi các thư mục ứng dụng, dependency files và cấu hình môi trường được đưa vào repository.

## Kiểm thử và CI

GitHub Actions chạy khi có push, pull request hoặc chạy thủ công. Workflow tại [`.github/workflows/ci.yml`](.github/workflows/ci.yml) sẽ:

- Cài dependency backend từ `backend/requirements.txt` và chạy `pytest` khi có test trong `backend/tests/`.
- Cài dependency frontend bằng `npm ci`, sau đó chạy các script `lint`, `typecheck` và `build` nếu được khai báo trong `frontend/package.json`.
- Cài Chromium và chạy Playwright khi có cấu hình `frontend/playwright.config.*` cùng test trong `frontend/tests/`.

Các lệnh kiểm thử tương ứng:

```bash
# Backend
cd backend
python -m pytest -q tests

# Frontend checks
cd ../frontend
npm ci
npm run lint
npm run typecheck
npm run build

# End-to-end tests (sau khi cấu hình Playwright)
npx playwright test
```

Playwright cần có cấu hình `webServer` để khởi động ứng dụng trước khi chạy test. CI bỏ qua phần frontend/backend chưa được thêm vào repository; khi các thư mục và test tương ứng xuất hiện, các bước sẽ tự chạy.

## Quy ước cộng tác

- Tạo feature branch cho từng hạng mục và mở pull request trước khi merge vào nhánh chính.
- Cần ít nhất một thành viên review pull request trước khi merge.
- Cập nhật tiến độ và blocker trên Jira theo workflow `To Do → In Progress → In Review → Done`.
- Chỉ dùng dữ liệu học sinh giả lập trong phát triển và demo. Không đưa mật khẩu, API key hoặc dữ liệu sức khỏe thật lên repository.
- Nội dung AI chỉ có tính hỗ trợ, không thay thế chẩn đoán hay quyết định của chuyên gia y tế.
