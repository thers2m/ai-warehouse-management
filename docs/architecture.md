# Kiến trúc

Vue 3 (SPA) -> Flask REST API -> Service/Repository -> Supabase PostgreSQL.

AI Agent (sau này) -> tool calling -> dùng chung Business Services; không gọi SQL trực tiếp.

Giai đoạn scaffold chỉ có read-only GET products, orders, inventory và GET health.
Chưa có auth/RBAC, approve order, transactional stock change hoặc LLM. Không triển khai trực tiếp lên production.
