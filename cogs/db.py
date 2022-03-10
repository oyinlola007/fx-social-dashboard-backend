import sqlite3

import cogs.config as config

conn = sqlite3.connect(config.DATABASE_NAME, check_same_thread=False)
conn2 = sqlite3.connect(config.DATABASE_NAME2, check_same_thread=False)


def get_affiliate_paid():
    ll = conn.execute(f"SELECT a.discord_id, a.amount_btc, a.time_stamp, b.username, b.avatar_url from AFFILIATE_PAID as a INNER JOIN USER_DETAILS as b on a.discord_id = b.discord_id")
    json_list = []
    for row in ll:
        data = {}
        data["discord_id"] = row[0]
        data["amount"] = row[1]
        data["time_stamp"] = row[2]
        data["username"] = row[3]
        data["avatar_url"] = row[4]
        json_list.append(data)
    return json_list

def get_sum_affiliate_paid():
    return conn.execute(f"SELECT SUM(amount_btc) from AFFILIATE_PAID").fetchone()[0]

def get_affiliate_to_pay():
    ll = conn.execute(f"SELECT a.discord_id, a.amount_btc, b.username, b.avatar_url from AFFILIATE_TO_PAY as a INNER JOIN USER_DETAILS as b on a.discord_id = b.discord_id")
    json_list = []
    for row in ll:
        data = {}
        data["discord_id"] = row[0]
        data["amount"] = row[1]
        data["username"] = row[2]
        data["avatar_url"] = row[3]
        json_list.append(data)
    return json_list

def get_sum_affiliate_to_pay():
    return conn.execute(f"SELECT SUM(amount_btc) from AFFILIATE_TO_PAY").fetchone()[0]

def get_active_members():
    ll = conn.execute(f"SELECT a.discord_id, a.expiry_date, b.username, b.avatar_url from ACTIVE_MEMBERS as a INNER JOIN USER_DETAILS as b on a.discord_id = b.discord_id")
    json_list = []
    for row in ll:
        data = {}
        data["discord_id"] = row[0]
        data["expiry_date"] = row[1]
        data["username"] = row[2]
        data["avatar_url"] = row[3]
        json_list.append(data)
    return json_list

def get_on_trial():
    ll = conn2.execute(f"SELECT * from ON_TRIAL")
    json_list = []
    for row in ll:
        try:
            data = {}
            data["discord_id"] = row[0]
            data["email"] = row[2]
            data["trial_end_time"] = row[3]
            val = get_user_data(row[0])
            data["username"] = val[0]
            data["avatar_url"] = val[1]
            json_list.append(data)
        except:
            pass
    return json_list

def get_user_data(discord_id):
    data = []
    for row in conn.execute(f"SELECT * from USER_DETAILS where discord_id = '{discord_id}'"):
        data.append(row[1])
        data.append(row[2])
    return data

def get_leaderboard():
    ll = conn.execute(f"SELECT b.INVITER, SUM(a.AMOUNT_USD) as sum, c.USERNAME, c.AVATAR_URL from SUCCESSFUL_TRANSACTIONS as a INNER JOIN INVITES as b ON a.DISCORD_ID = b.INVITEE INNER JOIN USER_DETAILS AS c ON b.INVITER = c.DISCORD_ID GROUP BY b.INVITER ORDER BY sum DESC LIMIT 10 ")
    json_list = []
    for row in ll:
        data = {}
        data["discord_id"] = row[0]
        data["total_amount"] = row[1]
        data["username"] = row[2]
        data["avatar_url"] = row[3]
        json_list.append(data)
    return json_list

def get_invites():
    ll = conn.execute(f"SELECT a.invitee, a.inviter, a.sub_status, a.time_stamp, b.username, b.avatar_url, c.username, c.avatar_url from INVITES as a INNER JOIN USER_DETAILS as b on a.invitee = b.discord_id INNER JOIN USER_DETAILS as c on a.inviter = c.discord_id ORDER BY a.TIME_STAMP DESC")
    json_list = []
    for row in ll:
        data = {}
        data["invitee_id"] = row[0]
        data["invitee_name"] = row[4]
        data["invitee_avatar_url"] = row[5]
        data["inviter_id"] = row[1]
        data["inviter_name"] = row[6]
        data["inviter_avatar_url"] = row[7]
        if row[2] == "0":
            data["sub_status"] = "Not Subscribed"
        else:
            data["sub_status"] = "Subscribed"
        data["date_joined"] = row[3]
        json_list.append(data)
    return json_list

