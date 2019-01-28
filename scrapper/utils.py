import sys
import re

is_well_formed_link = re.compile(r'^https?://.+/.+$')
is_root_path = re.compile(r'^/.+$')


def build_link(host, link):
    if not link:
        return link
    elif is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host, link)
    else:
        return '{host}/{uri}'.format(host=host, uri=link)


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = u"\u2588" * filled_len + u"\u2591" * (bar_len - filled_len)

    print('\r[%s] %s%s ...%s' % (bar, percents, '%', status), end='\r')
    if count == total:
        print()
