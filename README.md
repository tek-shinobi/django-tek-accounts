# django_accounts
--------------------
Django app for custom user model.

Just drop it in your project and add 'accounts' to settings.INSTALLED_APPS like this:

<pre>
<code>
INSTALLED_APPS = [
    ...
    'accounts',
]
</code>
</pre>


This will create a custom user with email as the required field. It will also configure the UserAdmin to show the custom user.

Run ``python manage.py migrate`` to generate the custom user model.

Use __pytest__ for testing. The tests will be picked up from tests/ directory.
