from typing import Any

from starlette.exceptions import HTTPException


class Responses:
    __original_attrs = {}

    @classmethod
    def get_responses(cls) -> dict[int | str, dict[str, Any]] | None:
        responses_dict = {}
        for attr in dir(cls):
            if not attr.startswith("__") and not callable(getattr(cls, attr)) and not attr.startswith("_"):
                try:
                    status_code, detail = getattr(cls, attr)
                    cls.__original_attrs[attr] = status_code, detail
                except Exception:  # noqa No matter what exception catches
                    status_code, detail = cls.__original_attrs[attr]
                if status_code not in responses_dict.keys():
                    responses_dict[status_code] = {
                        "description": attr.replace("_", " "),
                        "content": {"application/json": {"examples": {}}},
                    }

                responses_dict[status_code]["content"]["application/json"]["examples"][attr.lower()] = {
                    "summary": attr.replace("_", " "),
                    "value": {"detail": detail},
                }

                setattr(cls, attr, HTTPException(status_code=status_code, detail=detail))
        return responses_dict or None
