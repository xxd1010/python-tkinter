# 从网络获取时间戳


def getTime():
    responce = requests.get("https://www.tsa.cn/time.jspx")
    return responce.json()

# 网络请求
# 看能不能实现登录百度


def urlRequest():

    tt = getTime()  # 服务器时间
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36 Edg/88.0.705.56",
        "Accept": "atext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Host": "wappass.baidu.com",
    }
    name = "想"
    passwd = "123456abc"
    data = {
        "name": name,
        "password": passwd,
        "time": f"{tt/1000}",
        "tt": f"{tt}"
    }
    data = urllib.parse.urlencode(data)
    antireplaytoken = f"https://wappass.baidu.com/wp/api/security/antireplaytoken?baiduId=6759F3479F7CAE7EEE0ED6F1FC10A7C9%3AFG%3D1&tpl=undefined&tt={tt}"
    login = "https://wappass.baidu.com/wp/api/login"
    check = "https://wappass.baidu.com/v3/login/api/check"

    url_get_publickey = "https://passport.baidu.com/v2/getpublickey"

    session = requests.session()
    params = {"tt": f"{tt}", "time": f"{tt/1000}"}
    responce = session.request('get', url_get_publickey, cookies=requests.cookies.RequestsCookieJar(
    ), data=urllib.parse.urlencode(params))

    fp = "./temp.json"

    res = responce.content.decode('utf-8')

    # res = eval("{}".format(res))

    # dic = json.dumps(res)
    # ----->
    # dic = json.dumps(eval(res))
    # dic = json,loads(dic)

    # -------------json模块处理字符串时，字符串内不能使用'单引号 将单引号替换成双引号
    # new_res = res.replace("'", '"')
    # -------------eval()   太智能了,这里将 str--->---dict
    dic_pubkey = eval(res)

    # 正则匹配还行
    # pattern = r"-----BEGIN PUBLIC KEY-----\n(.*?)\n-----END PUBLIC KEY-----"

    # pattern = re.compile("{(.*?)}")
    # r = pattern.match(res)

    # with open(fp, 'r') as f:
    #     tmp = f.read()
    #     print(tmp)
    #     dic = json.load(f)
    # dic = json.loads(dic)

    print(tt, dic_pubkey['pubkey'], dic_pubkey['key'])

    # for name, value in responce.cookies.items():
    #     header['Cookie'] + f"{name}={value};"
    #     print(header)
    res = session.request('post', login, headers=header,
                          data=data, cookies=responce.cookies)
    json_res = res.json()


def rsa():

    pass


def baiduRequests():

    user_agent = "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0"

    ak = "1e3f2dd1c81f2075171a547893391274"
    as_ = ''
    tk = ''
    ds = ''
    baiduid = ''

    headers = {
        "UserAgent": user_agent,
    }
    # 进行URL编码
    header_encode = urllib.parse.urlencode(headers)

    tt = getTime()
    time = tt/1000

    session = requests.session()

    data_pubkey = {
        "tt": tt,
        "time": time
    }

    # url = "http://passport.baidu.com/passApi/js/wrapper.js"
    # url = "http://passport.baidu.com/static/phoenix/scripts/jssdk/all.js?v=" + f"{tt}"
    # url = "https://wappass.baidu.com/static/machine/js/api/mkd.js?cdnversion=1612412014921"
    url = f"https://passport.baidu.com/viewlog?callback=jQuery110204490579422128027_1612413745112&ak={ak}&_={tt}&as={as_}&ds={ds}&tk={tk}"
    pubkey_url = f"https://passport.baidu.com/v2/getpublickey{data_pubkey}"
    responce_pubkey = session.get(pubkey_url)
    pubkey = eval(responce_pubkey.content.decode('utf-8'))
    responce = session.request('get', url, headers=headers)
    cookies = session.cookies.items()
    baiduid = session.cookies.get('BAIDUID')
    # responce.content str 类型
    content = responce.content.decode('utf-8')
    content = content.replace('\\', '')
    content = content.replace('{', ' {')
    content = content.replace('}', '} ')

    # 匹配规则内带括号 需要对括号转义
    pattern = re.compile(r'\((.*?)\)')
    # print(responce.content)

    jQuery = re.findall(pattern, content)
    if jQuery != None:
        # jQuery = jQuery.group()
        jQuery = jQuery[0]
        # jQuery = jQuery.replace("'", '"')
        # jQuery = list(jQuery)
        # jQuery.insert(0, '{')
        # jQuery.insert(-1, '}')
        # jQuery = "".join(jQuery)
        jQuery = json.loads(jQuery)

    # print(responce.content.decode('utf-8'))
    # print(pubkey['pubkey'])
    # print(cookies)

    tk = jQuery['data']['tk']
    as_ = jQuery['data']['as']
    ds = jQuery['data']['ds']
    # print(f"{tk}\n{as_}\n{ds}")

    tt = getTime()
    time = tt/1000

    username = "gihdf"
    # passwd = "123456"
    # passwd = "gDnsfEp/qRRAjWsIVaSwwNA25zCJ07Bmn7AQef9Rq0X96QrohcmAuSC/JnT7jR3uBXby/EbI/GBNzSbofV/SVfsUZ2+1/WAIa1/KTkFTd/mG2WIA+d8EDu3wzTZmM6TABloYnzjwXS0OjIZD2TvwP6w1gxRmoxDJJ8kftiDwldU="
    passwd = "gZDHQ8EAY0gvBCqA7FbjDHvG4/sWkU/eYKT9IGM327x3lF/GZ/cMBEQciNFJCWq43tFyvH0mfNctzNDqJGjc3jd3Pv/JOYNM0JmtlrUBLBA7W1NL0wSw3/xqFf3FUe5KBE0Rq9Aw7GnkWe9QESlYxvxu5BfYMWrNEO6aNmV5RZg="

    data = f"tk={tk}&ds={ds}&baiduid={baiduid}&tt={tt}&time={time}&user={username}&password={passwd}"
    data_ = {
        'tk': tk,
        'ds': ds,
        'baiduid': baiduid,
        'tt': tt,
        'time': time,
        'user': username,
        'password': passwd,
        # 'fuid': 'FOCoIC3q5fKa8fgJnwzbE3sZaS3poGTofPItBD67MTHOloTQtOTfZukshuG+jikLjcNlSm6rsdxc/uQOWSQ3rfMTzSxzVsGQwG0e2jODBNzRN3di3mJZApaNdmihpvjP7hw25jTiOJFGuwYgKNR+Z4z7TMXRylEW5hdNFYaBjuCuFMYVIsOGCDcCGm/hArLqSOgoap6LII1odh53KcPUGEzAXw/4G8X7zorxMJyyaQkGdDCFhDp1FTg9fg9vNAxZRSNi0EmYXex3t184x2vmzefloBCVK8P9aR2PgTjdHWEJhIHoCf1vrT/LBXFZciAmptcggmzYn+CIvybFwsZjwHfnhF2UPd1L1q+jU7GytGuFOJMonj8HeGxWING5SpTw8KYSkBKlpsZTAl9/HTsKfA9lhvCbfCr9VrwCWD+8yFo7Zp7+/tcB/67VNuOV0qiZQbeCqJ91LNPfk1CUv8oZVv27yY+1LcXpa/MZXWzU+38ZicwLx3tTw8w2MT/zIqkrVGxc/andre2Cb054eMI7rHlS9TRCSVaPBPvpXMrEnoLRvikV1UgzYy9ZTpTyZXoyxN82eMOBuxXq32VXPeMikjYhSBNv3w+demMvj+QP5SlydVZ20MQJep85qF11fe+pfD3TxZm501QAqXUk0wQakx6sUA2b8gb1zDetzYySo+crkotJYde4FfDY9kEl5jI/4bADxDhcJI4rKyJj2nz9TL8iiLPyKq/JhjaMdm6zVOO/jW0KOye67IIGr6eTdIqqmqtCZ4e5FbkdlgZa7f+zEr0DmY2bfhk+6hFX7NjcWSF9F/BTuSXYBdWiXpj3boOOco0gRxKbmmfHkzAOXVTmWX8ztnJsOS+HVUzWuZcBI/51EZKW6ozgW4CAcK92ep8aedt7e+wercu4XumiZtPrl/M71s426so1pL4xtIUIZnkkQ66KpQyCTZXEtxIcd/UQRk//Dw3a1TfmjGWx6rUtaA+7pe20aBIMPerN5P6KgZGVWGjCp19HVoeRO1Z4akUiKdupxdT9Ph/aEsgj0PeDz9UkWmq0qFdIPf5nF710yii9on7w7ZrwWg4DrUA1B1pInWBqDRlBh76FBhFXrhjb3vs/UeWUb8BQF4HOmgDpdvIC1uVZd2elfyJmpTQUiDgJC+xWQc46DVC8U6X4XwrKeM0bM3mLxclwj0rieaMqDoKAjylxPH1+91jmdJgJRdZn',
        'gid': 'FE1CF80-7428-46C7-A4A8-B7C1CC499A45',
        'session_id': 'FE1CF80-7428-46C7-A4A8-B7C1CC499A45-v2-1612420278022-password_login',
        'sig': 'N1Y1TFNFVzJYK2Y5YnR3UUdwNmlOdXFGVDNTS05NRVJ0WXZySDNVTG8rMTVVRVl0ejc5bE1GdTNremVVYnFIKw==',
        # 'shaOne': '007f6997d209b6b824346b9372b39cc70eabb47b',
        # 'moonshad': '28ad427f97ea32c30do0a5ea2a287d81e9',
        'u': 'http%3A%2F%2Fwww.baidu.com%2F'
    }
    url = "https://wappass.baidu.com/wp/api/login?"
    checkurl = "https://wappass.baidu.com/v3/login/api/check?"
    check = session.post(checkurl, data=data_)
    responce = session.request('post', url, headers=headers, data=data)
    cookies = session.cookies.items()
    print(json.loads(responce.content.decode('unicode_escape').replace('\\', '')))
    print(cookies)


class w():
    isNeg = False
    digits = []
    for i in range(131):
        digits.append(0)


def B(e, t):
    if e.isNeg != t.isNeg:
        t.isNeg = not t.isNeg
        n = I(e, t)
        t.isNeg = not t.isNeg
    else:
        n = w()
        s = 0
        for o in range(len(e)):
            i = e.digits[o] - t.digits[o] + s
            n.digits[o] = 65535 & i
            n.digits[o] = n.digits[o] + g
            if i < o:
                var1 = 1
            else:
                var1 = 0
            s = 0-var1
        if -1 == s:
            s = 0
            for o in range(len(e.digits)):
                i = 0 - n.digits[o] + s
                n.digits[o] = 65535 & i
                n.digits[o] = n.digits[o] + g
                if i < o:
                    var1 = 1
                else:
                    var1 = 0
                s = 0-var1
            n.isNeg = not e.isNeg
        else:
            n.isNeg = e.isNeg
    return n


def L(e):
    u = []
    for i in range(131):
        u.append(0)
    t = u
    e_ = e
    n = len(e.digits)
    for i in range(n):
        # print('n:', n)
        max_index = max(n - 4, 0)
        min_index = min(n, 4)
        # print("max:{} min:{}".format(max_index, min_index))
        if n > 0:
            # 10001
            e_.digits = e.digits[max_index:max_index+min_index]
            # print('e_.digits:', e_.digits)
            t[i] = F(e_)
            n = n - 4
        else:
            break
    return t


def P(e):
    t = len(e.digits) - 1
    while (t > 0 and 0 == e.digits[t]):
        t = t - 1
    return t


def a(e):
    result = H(dollar(H(e, k-1), mu), k+1)
    n = B(K(e, k+1), K(dollar(t, modulus), k+1))
    n = I(n, bkplus1)
    var1 = q(n, modulus) >= 0
    while(var1):
        n = B(n, modulus)
        var1 = q(n, modulus) >= 0
    return n


def r(e, t):
    n = dollar(e, t)
    return modulo(n)


def o(e):
    modulus = e
    k = P(modulus) + 1
    # t = m
    # n = d
    u = []
    for i in range(131):
        u.append(0)
    i = u
    i[2 * k] = 1

    t = i
    n = modulus
    var1 = z(t, n)[0]
    mu = [t, n, var1]

    modulo = a()
    multiplyMod = r()
    powMod = c


def z(e, t):
    h = 16
    v = 32768
    g = 65536
    # t.isNeg  False
    u = []
    for i in range(131):
        u.append(0)

    s = E(e)
    o = E(t)
    a = t.isNeg
    if (s < o):
        # return e.isNeg ? ((n = b(p)).isNeg = !t.isNeg,
        #         e.isNeg = !1,
        #         t.isNeg = !1,
        #         i = B(t, e),
        #         e.isNeg = !0,
        #         t.isNeg = a) : (n = new w,
        #         i = b(e)),
        n = b(p)

        # return n.isNeg is  not t.isNeg

        n = u
        i = b(e)
        # 数组拼接
        new = n + i
        return new
    n = u
    i = e
    r = math.ceil(o/h)-1
    c = 0
    if t[r] < v:
        t = U(t, 1)
        c = c+1
        o = o+1
        r = math.ceil(o/h)-1
    i = U(i, c)
    s = s+c
    u = math.ceil(s/h)-1
    l = R(t, u-r)
    while -1 != q(i, 1):

        i = B(i, 1)

        n[u-r] = n[u-r]+1
    d = u
    while d > u:

        if d >= len(i):
            y = 0
        else:
            y = i[d]

        if d-1 > len(i):
            _ = 0
        else:
            _ = i[d-1]

        if d-2 > len(i):
            C = 0
        else:
            C = i[d-2]
        if r >= len(t):
            k = 0
        else:
            k = t[r-1]
        if r-1 >= len(t):
            T = 0
        else:
            T = t[r-1]
        # python 三元条件运算符
        # 语句一 if 条件 else 语句二
        n[d-r-1] = (m if y == k else math.floor((y*g+_)/k))
        x = n[d-r-1]*(k*g+T)
        N = y*f+(_*g+C)
        while x > N:
            x = n[d-r-1] * (k*g | T)
            N = y*g*g+(_*g+C)
            n[d-r-1] = n[d-r-1]-1

        l = R(t, d-r-1)
        i = B(i, O(l, n[d-r-1]))

        False & (I(i, 1))

        d = d - 1


g = 65536
radix = 16
chunk_size = 0
modulus = w()
k = P(modulus) + 1
t = 0

mu = []
bkplus1 = w()
bkplus1.digits[k+1] = 1
modulo = ''
multiplyMod = ''
powMod = ''


def X(e, t, n):
    g = 65536

    e = L(e)
    d = L(t)
    m = L(n)
    radix = 16
    chunk_size = 2 * P(m)

    modulus = w()
    k = P(modulus) + 1
    t = m

    mu = []
    bkplus1 = w()
    bkplus1.digits[k+1] = 1
    modulo = ''
    multiplyMod = ''
    powMod = ''


def str2Ascii(e, t):
    u_ = []
    for i in range(131):
        u_.append(0)
    t = u_
    n = len(t)
    for i in range(n):
        n[i] = ord(t[i])
    s = 0
    while (len(n) % e.chunk_size != 0):
        s = s + 1
        n[s] = 0
    o = 0
    c = len(n)
    u = ""
    s = 0
    while (s < c):
        r = u
        a = s
        while (a < s + e.chunk_size):
            a = a + 1
            r[o] = n[a]
            r[o] = n(a) << 8

            o = o + 1


def U(e, t):
    h = 16
    n = math.floor(t/h)
    u = []
    for i in range(131):
        u.append(0)
    i = u
    V(e, 0, i, n, len(i)-1)
    s = t % h
    o = h - s
    a = len(i) - 1
    r = a - 1
    while a > 0:
        i[a] = i[a] << s & m | (i[r] & D[s] >> o)
        a = a-1
        r = r-1
    i[0] = i[a] << s & m
    return i


def V(e, t, n, i, s):
    o = min(t+s, len(e))
    a = t
    r = i
    while(a < o):
        n[r] = e[a]
        a = a+1
        r = r+1


def R(e, t):
    u = []
    for i in range(131):
        u.append(0)
    n = u
    V(e, 0, n, t, len(n)-t)
    return n


def E(e):
    h = 16
    n = P(e)
    i = e[n]
    s = (n+1)*h
    t = s
    while(t > s-h and 0 == (32768 & i)):
        i = i << 1
        t = t-1
    return t


def b(e):
    t = e
    return t


def q(e, t):
    n = len(e)-1
    while n >= 0:
        n = n-1
    return 0


def B(e, t):
    return False


def O(e, t):
    u = []
    for i in range(131):
        u.append(0)
    o = u
    n = P(e)
    i = 0
    for a in range(n+1):
        s = o[a] + e[a]*t+i
        o[a] = s & m
        i = s >> d
    o[1+n] = i
    return o


def I(e, t):
    pass


def dollar(e, t):
    u = []
    for i in range(131):
        u.append(0)
    o = u

    a = P(e)
    r = P(e)
    c = 0
    while(c <= r):
        n = 0
        s = c
        u = 0
        while (u <= a):
            i = o[s] + e[u] * t[c] + n
            o[s] = i & m
            n = i >> d
            u = u + 1
            s = s + 1
        c = c + 1
        o[c+a+1] = n
    return o


def S(e):
    if e >= 48 and e <= 57:
        e = e - 48
    else:
        if e >= 65 and e <= 90:
            e = 10 + e - 65
        else:
            if e >= 97 and e <= 122:
                e = 10 + e - 97
            else:
                e = 0
    # print(e)
    return e


def W(e, t):
    u_ = []
    for i in range(131):
        u_.append(0)
    n = u_
    i = len(t)
    s = 0
    while s < i:
        n[s] = ord(t[s])
        s = s + 1

    while len(n) % e.chunk_size != 0:
        s = s + 1
        n[s] = 0
    c = len(n)
    u = ''
    while s < c:
        r = w()
        o = 0
        a = s
        while a < s+e.chunk_size:
            a = a + 1
            r.digits[o] = n[a]
            r.digits[o] = r.digits[o] + n[a] >> 8

            o = o + 1
        l = e.barrett.powMod(r, e.e)
        s = s + e.chunk_size


def F(e):
    t = 0
    n = min(len(e.digits), 4)
    for i in range(n):
        # 按位与   ( bitwise and of x and y )
        # &  举例： 5&3 = 1  解释： 101  11 相同位仅为个位1 ，故结果为 1
        # 按位或   ( bitwise or of x and y )
        # |  举例： 5|3 = 7  解释： 101  11 出现1的位是 1 1 1，故结果为 111
        # 按位异或 ( bitwise exclusive or of x and y )
        # ^  举例： 5^3 = 6  解释： 101  11 对位相加(不进位)是 1 1 0，故结果为 110
        # 按位反转 (the bits of x inverted )
        # ~  举例： ~5 = -6  解释： 将二进制数+1之后乘以-1，即~x = -(x+1)，-(101 + 1) = -110
        #     按位反转仅能用在数字前面。所以写成 3+~5 可以得到结果-3，写成3~5就出错了
        # 按位左移 （ x shifted left by n bits ）
        # << 举例:  5<<2 = 20 解释：101 向左移动2位得到 10100 ，即右面多出2位用0补
        # 按位右移 （ x shifted right by n bits ）
        # >> 举例： 5>>2 = 1  解释：101 向右移动2位得到 1，即去掉右面的2位
        # 左移运算符

        # ord 字符-->ascii码
        s = S(ord(str(e.digits[i])))
        t = t << 4 | s
        # print(s, t)
    return t


passwd = "admin123d4a1763953"

D = [0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280,
     65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535]
M = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511,
     1023, 2047, 4095, 8191, 16383, 32767, 65535]
G = 'B3C61EBBA4659C4CE3639287EE871F1F48F7930EA977991C7AFE3CC442FEA49643212E7D570C853F368065CC57A2014666DA8AE7D493FD47D171C0D894EEE3ED7F99F6798B7FFD7B5873227038AD23E3197631A8CB642213B9F27D4901AB0D92BFA27542AE890855396ED92775255C977F5C302F1E7ED4B1E369C12CB6B1822F'

# e_str = "10001"
# t = ''
# n = G


# print(e.digits, e.isNeg)
# e = w()
# e.digits = "10001"
# e = L(e)
# t = w()
# t.digits = ''
# d = L(t)
# n = w()
# n.digits = G
# m = L(n)

# radix = 16
# print(e)
# print(d)
# print(m)

# print(type(e) == 'bool')

js_env = execjs.get()

vender = open("./baidu/0003.js", mode='r', encoding='utf-8').read()
vender = js_env.compile(vender)
func = ""

passport = open("./baidu/0004.js", 'r', 'utf-8').read()
passport = js_env.compile(passport)
vender()
passport()