# @Version  :1.0
# @Author   :李祎凡
# @File     :test2
# @Time     :2025/3/19 下午3:41
# @Other    :爬百度
import requests

url =  'https://fanyi.baidu.com/sug'


data = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
'cookie':'BAIDUID_BFESS=281F3DBD48205DB8FDFB3DCC73AC5C7B:FG=1; BIDUPSID=281F3DBD48205DB8FDFB3DCC73AC5C7B; PSTM=1742357679; BDRCVFR[BIVAaPonX6T]=-_EV5wtlMr0mh-8uz4WUvY; H_PS_PSSID=61027_61672_62325_62344_62345_62365_62371_62421_62423_62426_62473_62457_62455_62453_62451_62618_62643; BA_HECTOR=0k218k0520250l24al2g818004mk6g1jtkh5g22; ZFY=VWc6tSEYDxpdFZYppuGYWI3yigeFce5etOWxnFGS61E:C; PSINO=1; delPer=0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_WISE_SIDS=61027_61672_62325_62344_62345_62365_62371_62421_62423_62426_62473_62457_62455_62453_62451_62618; ab_sr=1.0.1_OWI0MzBmMmI0ZmQ2MDIzMjRmMjBkMjZiM2RlMWJiYjM3YzNmMGM4NTZjN2U5ZjZjNWU2NDIxMTc3ZTlkNTU1N2IyOGE2YWJiMDUzNDRhNGQ4ZGYyMjE3MTY4MjZlMTY3ZWJkYmE0ZTQwMWM0OGNhZWZkNTI2ZTIyZjYwM2Y1NmRhNjZmMDM3ZGNjY2FkZDczY2NiZTExZDk1YjFmYmU4ODc4NjAxYjg4YzM2MWExNDg1MmMyYWY5OTAyZDBmNTgwNGIxZTAxNDJmMTAyMWUzNDRkNWZhMDRmMTMwY2M3ZjE=; RT="z=1&dm=baidu.com&si=730bb636-0661-49e1-8d47-b142e73b6299&ss=m8fm3zbr&sl=1&tt=18r&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=a40k"',
    'kw':'猫'
}

res = requests.post(url,data=data)
print(res.json())