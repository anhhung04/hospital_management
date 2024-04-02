from fastapi import HTTPException, status


def permit(acl):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user = args[0]._current_user
            for ac in acl:
                allow, role = ac
                if user.get("role", None) == role and allow:
                    return func(*args, **kwargs)
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied")
        return wrapper
    return decorator
