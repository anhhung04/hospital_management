from fastapi import HTTPException, status


def permit(acl):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user = args[0]._current_user
            role = user.get("role", None)
            if role and role in acl:
                return func(*args, **kwargs)
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied")
        return wrapper
    return decorator
