from fastapi import HTTPException, status
from permissions.user import UserRole


class Permission:
    def __init__(self, current_role="user"):
        self._role = str(current_role).upper().split(":")

    @staticmethod
    def permit(superACL, acl=[]):
        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    user = args[0]._current_user
                    assert user
                except Exception:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Forbidden"
                    )
                uc = [str(c).upper() for c in Permission(user.role())]
                if str(UserRole.ADMIN).upper() in uc:
                    return func(*args, **kwargs)
                for ac in superACL:
                    if str(ac).upper() in uc:
                        return func(*args, **kwargs)
                for ac in acl:
                    if str(ac).upper() in uc and user.id() == kwargs.get("id"):
                        return func(*args, **kwargs)

                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Permission denied"
                )
            return wrapper
        return decorator

    @staticmethod
    def has_role(role, user):
        uc = [str(c).upper() for c in user.role().split(":")]
        for ac in role:
            if str(ac).upper() in uc:
                return True
        return False

    def add(self, role):
        self._role.append(str(role).upper())
        return self

    def get(self):
        return ":".join(self._role)

    def delete(self, role):
        self._role.pop(role)
        return self

    def __iter__(self):
        for role in self._role:
            yield role
