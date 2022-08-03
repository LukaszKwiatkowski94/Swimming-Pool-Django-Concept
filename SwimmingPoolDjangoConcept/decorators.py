from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

def administrator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    decorator = user_passes_test(
        lambda u: u.is_active and u.role==2,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return decorator(function)
    return decorator

def cashier_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    decorator = user_passes_test(
        lambda u: u.is_active and u.role==3,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return decorator(function)
    return decorator

def customer_service_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    decorator = user_passes_test(
        lambda u: u.is_active and u.role==4,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return decorator(function)
    return decorator

def accountant_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    decorator = user_passes_test(
        lambda u: u.is_active and u.role==5,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return decorator(function)
    return decorator

def press_spokesman_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    decorator = user_passes_test(
        lambda u: u.is_active and u.role==6,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return decorator(function)
    return decorator

def management_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    decorator = user_passes_test(
        lambda u: u.is_active and u.role==7,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return decorator(function)
    return decorator