curl -LsSf https://astral.sh/uv/install.sh | sh

uv init --package .

uv sync

uv run alembic revision --autogenerate -m "initial schema"

uv run alembic upgrade head