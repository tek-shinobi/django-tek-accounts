# django-tek-accounts
--------------------
Django accounts app for custom user model.

__Step 1__: Create new project. 

__Step 2__: Drop __accounts__ folder as an app into your project and add 'accounts' to settings.INSTALLED_APPS like this:

<pre>
<code>
INSTALLED_APPS = [
    ...
    'accounts',
]
</code>
</pre>


In the same ``settings.py`` file, add the custom user model by adding this line at the bottom:
<pre>
<code>
AUTH_USER_MODEL = 'accounts.User'
</code>
</pre>

__Step3__: Run ``python manage.py migrate`` to generate the custom user model.

This will create a custom user with email as the required field. It will also configure the UserAdmin to show the custom user.

Use __pytest__ for testing. The tests will be picked up from tests/ directory.
