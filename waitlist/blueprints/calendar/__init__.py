from waitlist.blueprints.settings import add_menu_entry
from waitlist.permissions import perm_manager
from flask_babel import lazy_gettext

perm_manager.define_permission('calendar_event_add')

add_menu_entry('calendar_settings.get_index', lazy_gettext('Events'),
               perm_manager.get_permission('calendar_event_add').can)
