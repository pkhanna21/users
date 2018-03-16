from constants import default_limit,default_page

select_user_query = '''SELECT * FROM users '''
delete_user_query = '''DELETE FROM users '''
insert_user_query = '''INSERT INTO users (first_name, last_name, company_name, age, city, state, zip, email, web) values '''
update_user_query = '''UPDATE users SET '''

def get_user_by_id_query(id):
    return select_user_query + '''where id = ''' + id

def delete_user_by_id_query(id):
    return delete_user_query + '''where id = ''' + id

def insert_user(first_name, last_name, company_name, age, city, state, zip, email, web):
    return insert_user_query\
           + '''("''' + first_name + '''",'''\
           + '''"''' + last_name + '''",'''\
           + '''"''' + company_name + '''",'''\
           + str(age) + ''','''\
           + '''"''' + city + '''",'''\
           + '''"''' + state + '''",'''\
           + str(zip) + ''','''\
           + '''"''' + email + '''",'''\
           + '''"''' + web + '''")'''

def update_user_by_id(id, first_name, last_name, company_name, age, city, state, zip, email, web):
    return update_user_query\
           + '''first_name = "''' + first_name + '''",''' \
           + '''last_name = "''' + last_name + '''",''' \
           + '''company_name = "''' + company_name + '''",''' \
           + '''age = ''' + str(age) + ''',''' \
           + '''city = "''' + city + '''",''' \
           + '''state = "''' + state + '''",''' \
           + '''zip = ''' + str(zip) + ''',''' \
           + '''email = "''' + email + '''",''' \
           + '''web = "''' + web + '''"''' \
           + ''' WHERE id = ''' + str(id)

def get_name_query(name_string):
    if name_string is not None:
        return '''where first_name LIKE "%''' + name_string + '''%"''' +  ''' OR last_name LIKE "%''' + name_string + '''%"'''
    else:
        return ''''''

def order_by_query(field):
    if field is not None:
        return ''' ORDER BY ''' + field + '''''' + ''' ASC'''
    else:
        return ''''''

def get_offset(limit, page):
    if page is not None and limit is not None:
            return ''' OFFSET ''' + str(int(limit) * int(page)) + ''''''
    else:
        if page is not None and limit is None:
            return ''' OFFSET ''' + str(int(page) * int(default_limit)) + ''''''
        elif page is None and limit is not None:
            return ''' OFFSET ''' + str(int(default_page) * int(limit)) + ''''''
        else:
            return ''' OFFSET ''' + str(int(default_page) * int(default_limit)) + ''''''

def get_limit(limit):
    if limit is not None:
        return ''' LIMIT ''' + limit + ''''''
    else:
        return ''' LIMIT ''' + str(default_limit) + ''''''

def get_all_user_query(name_string, field, limit, page):
    return select_user_query + get_name_query(name_string) + order_by_query(field) + get_limit(limit) + get_offset(limit, page)