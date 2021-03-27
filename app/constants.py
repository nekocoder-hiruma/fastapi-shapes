def error_responses(model: str) -> dict:
    return dict({
        404: {
            "description": f"{model} Not Found"
        }
    })
