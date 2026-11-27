import sys, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, Polygon
for f in ['Light','Regular','Medium','Bold','Black']:
    fm.fontManager.addfont(f'/usr/share/fonts/opentype/noto/NotoSansCJK-{f}.ttc')
SANS='Noto Sans CJK JP'; MONO='DejaVu Sans Mono'
plt.rcParams.update({'font.family':SANS,'axes.unicode_minus':False})
MODE=sys.argv[1] if len(sys.argv)>1 else 'dark'
if MODE=='dark':
    BG='#0d1015'; FG='#ebe6da'; DIM='#9aa1ab'; FAINT='#2a2f38'; AMB='#f3a83b'
    BLD='#1e242e'; BLDE='#3a414d'; W0='#151a22'; W1='#ffd58a'; B03='#3a2a12'; DOT0='#4a515c'; DOT1='#8b929c'
    ISO=('#161b23','#1e242e','#2a313c'); ISOE='#3a414d'; GROUND='#12161d'; ISOA=('#b9761f',AMB,'#ffc96e')
else:
    BG='#f5f2eb'; FG='#15171c'; DIM='#4f5663'; FAINT='#cfc9bc'; AMB='#d07b06'
    BLD='#2b313b'; BLDE='#2b313b'; W0='#3c434e'; W1='#ffd58a'; B03='#6b4a1a'; DOT0='#c6c0b3'; DOT1='#8b929c'
    ISO=('#4a525e','#5d6672','#7a8390'); ISOE='#2b313b'; GROUND='#e7e2d7'; ISOA=('#a35f05',AMB,'#f2b04e')
pc={1990:127.8,1991:116.5,1992:104.6,1993:89.7,1994:69.5,1995:61.5,1996:55.9,1997:54.7,1998:54.1,1999:54.4,2000:58.1,2001:63.8,2002:67.8,2003:74.8,2004:84.2,2005:87.5,2006:94.7,2007:103.0,2008:105.8,2009:90.2,2010:94.2,2011:99.7,2012:100.0,2013:100.2,2014:95.1,2015:86.3,2016:88.9,2017:91.4,2018:95.1,2019:98.8,2020:95.8,2021:100.0,2022:77.3,2023:89.2}
tot={1990:159.1,1991:145.3,1992:130.9,1993:112.3,1994:86.6,1995:76.0,1996:68.4,1997:66.4,1998:65.1,1999:65.0,2000:68.8,2001:74.9,2002:78.9,2003:86.4,2004:96.5,2005:99.5,2006:107.0,2007:115.8,2008:118.4,2009:100.5,2010:104.6,2011:110.3,2012:110.5,2013:110.5,2014:99.4,2015:89.7,2016:91.9,2017:94.0,2018:97.3,2019:100.4,2020:96.7,2021:100.0,2022:71.2,2023:75.2}
fig=plt.figure(figsize=(16.54,23.39)); fig.patch.set_facecolor(BG)
def T(x,y,s,**k): fig.text(x,y,s,color=k.pop('color',FG),**k)
def hr(y,x0=0.05,x1=0.95,c=None,lw=1): fig.add_artist(plt.Line2D([x0,x1],[y,y],transform=fig.transFigure,color=c or FAINT,lw=lw))
def vr(x,y0,y1,c=None,lw=1): fig.add_artist(plt.Line2D([x,x],[y0,y1],transform=fig.transFigure,color=c or FAINT,lw=lw))
def style(ax):
    ax.set_facecolor('none')
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(colors=DIM,labelsize=13,length=0)
def label(x,y,num,txt):
    T(x,y,num,fontsize=16,color=AMB,fontfamily=MONO,fontweight='bold',va='center')
    T(x+0.045,y,txt,fontsize=17,color=AMB,fontweight='bold',va='center')

# ===== header =====
T(0.05,0.975,'개인 PRD  ·  개발도상국 분쟁과 경제 회복',fontsize=14,color=DIM,va='center')
T(0.95,0.975,'남서울대학교  임동하',fontsize=15,color=DIM,ha='right',va='center')
T(0.05,0.928,'전쟁은 경제를',fontsize=62,fontweight='light',va='center')
T(0.05,0.872,'몇 년 전으로 되돌리나',fontsize=62,fontweight='black',va='center',color=AMB)

# ===== 01 문제 (top-right) =====
vr(0.585,0.842,0.955,c=AMB,lw=2)
label(0.60,0.948,'01','문제')
T(0.60,0.920,'전쟁 피해는 "GDP −22.7%"처럼 보도된다.',fontsize=17,fontweight='bold',va='center')
T(0.60,0.897,'·  이 숫자로는 얼마나 잃었는지 체감되지 않는다',fontsize=14,va='center')
T(0.60,0.878,'·  어느 나라가 회복에 실패할지 가릴 기준이 없다',fontsize=14,va='center')
T(0.60,0.851,'→  잃은 경제를 "시간"으로 번역하고,\n     위험국을 미리 고를 수 있는지 검증한다',fontsize=14,va='center',color=AMB,fontweight='medium',linespacing=1.5)

# ===== 02 기능 1: skyline =====
hr(0.828)
label(0.05,0.812,'02','핵심 기능')
T(0.18,0.812,'기능 1  ·  후퇴 연수 — 경제를 시간으로 번역',fontsize=19,fontweight='bold',va='center')
ax=fig.add_axes([0.05,0.555,0.90,0.235]); style(ax)
yrs=list(pc)
for y in yrs:
    h=pc[y]; hl=y in (2022,2003); now=y==2021
    fc=AMB if y==2022 else (B03 if y==2003 else BLD)
    ec=AMB if hl else (FG if now else BLDE)
    ax.add_patch(Rectangle((y-0.42,0),0.84,h,fc=fc,ec=ec,lw=1.6 if hl or now else 0.6,zorder=2))
    for wy in np.arange(4,h-3,4.6):
        for wx in (-0.22,0.08):
            lit=((y*7+int(wy))%5==0)
            ax.add_patch(Rectangle((y+wx,wy),0.14,2.2,fc=(BG if y==2022 else (W1 if lit else W0)),ec='none',zorder=3))
for y in range(2004,2022):
    if pc[y]>77.3: ax.add_patch(Rectangle((y-0.42,77.3),0.84,pc[y]-77.3,fc=AMB,alpha=0.35,ec=AMB,lw=1,zorder=4))
ax.plot(yrs,[tot[y] for y in yrs],color=DIM,lw=1.4,ls=(0,(3,3)),zorder=4)
ax.axhline(77.3,color=AMB,lw=1.4,ls=(0,(2,3)),zorder=5)
ax.annotate('',xy=(2003.5,120),xytext=(2021.5,120),arrowprops=dict(arrowstyle='<->',color=AMB,lw=2))
ax.text(2012.5,124,'18 YEARS',ha='center',fontsize=30,fontweight='bold',color=AMB,fontfamily=MONO)
for y,lab in [(2003,'2003\n74.8'),(2021,'2021\n100'),(2022,'2022\n77.3'),(2023,'2023\n89.2')]:
    ax.text(y,pc[y]+3,lab,ha='center',va='bottom',fontsize=13,fontfamily=MONO,color=AMB if y in (2003,2022) else FG,zorder=6,
            bbox=dict(fc=BG,ec='none',pad=1) if y==2003 else None)
for y,lab,yl in [(1991,'1991 독립',140),(2009,'2009 금융위기',152),(2014,'2014 크림·돈바스',152),(2020,'2020 코로나',143),(2022,'2022 전면 침공',162)]:
    ax.plot([y,y],[pc[y]+1,yl-3],color=DIM,lw=0.7,ls=':',zorder=1)
    ax.text(y,yl,lab,ha='center',fontsize=13,color=AMB if y==2022 else DIM,bbox=dict(fc=BG,ec='none',pad=1.5),zorder=8)
ax.text(1996.5,62,'체제전환 붕괴',fontsize=12.5,color=DIM,ha='center',bbox=dict(fc=BG,ec='none',pad=1))
ax.set_xlim(1989.3,2023.7); ax.set_ylim(0,172); ax.set_xticks(range(1990,2024,5)); ax.set_yticks([])
for l in ax.get_xticklabels(): l.set_fontfamily(MONO)
ax.axhline(0,color=FG,lw=1.4,zorder=7)
T(0.05,0.534,'건물 = 한 해, 높이 = 우크라이나 1인당 실질 GDP 지수(2021 = 100).  점선 = GDP 총량.  반투명 호박색 = 전쟁 1년이 지운 높이.',fontsize=13,color=DIM,va='center')
T(0.05,0.518,'후퇴 연수 = 충격 후 최저점 이하였던 마지막 해까지 거슬러 올라간 햇수.  창문은 장식.',fontsize=13,color=DIM,va='center')
nums=[('18','년','1인당 실질 GDP 기준 후퇴','2022년 값 이하였던 마지막 해 = 2003'),
      ('21','년','GDP 총량 기준 후퇴','인구 유출로 1인당 수치는 덜 떨어져 보임'),
      ('5','년','반등 후에도 남은 후퇴','2023년 값도 2016년 수준 (2021년 기준)')]
for k,(n,u,a,b) in enumerate(nums):
    x=0.05+k*0.26
    T(x,0.468,n,fontsize=60,fontweight='black',color=AMB if k==0 else FG,va='center')
    T(x+0.085 if len(n)==2 else x+0.042,0.458,u,fontsize=24,fontweight='bold',color=AMB if k==0 else FG,va='center')
    T(x,0.428,a,fontsize=16,fontweight='bold',va='center')
    T(x,0.411,b,fontsize=13,color=DIM,va='center')
qa=fig.add_axes([0.852,0.403,0.098,0.068]); from PIL import Image as _I; qa.imshow(np.asarray(_I.open('qr.png').convert('RGB')),interpolation='nearest'); qa.axis('off'); qa.set_aspect('equal')
T(0.901,0.481,'폰으로 직접 해보기',fontsize=13,fontweight='bold',ha='center',va='center',color=AMB)
hr(0.395)

# ===== 기능 2 (left) =====
T(0.05,0.378,'기능 2  ·  분쟁 간 비교',fontsize=19,fontweight='bold',va='center')
T(0.05,0.360,'분쟁 발발 35건 (전투사망 1,000명 이상 · 24개국)에 같은 정의 적용',fontsize=13,color=DIM,va='center')
ax=fig.add_axes([0.05,0.298,0.42,0.05]); ax.axis('off')
known=sorted([55,47,37,23,14,12,11,9,6,6]); pts=[0]*15+[None]*10+known
for i,v in enumerate(pts):
    c=DOT0 if v==0 else (DOT1 if v is None else (AMB if v>=18 else FG))
    ax.add_patch(plt.Circle((i%18,1-i//18),0.38,color=c))
ax.set_xlim(-0.6,17.6); ax.set_ylim(-0.6,1.6); ax.set_aspect('equal')
lx=0.05
for c,l in [(DOT0,'0년 · 15건'),(DOT1,'1–6년 · 10건'),(FG,'6–14년'),(AMB,'23년 이상')]:
    T(lx,0.286,'●',fontsize=15,color=c,va='center'); T(lx+0.016,0.286,l,fontsize=12.5,color=DIM,va='center'); lx+=0.03+len(l)*0.0075
T(0.05,0.258,'중앙값 1년 — 대부분은 거의 되돌리지 않지만,\n소수는 수십 년을 지운다.',fontsize=16,fontweight='bold',va='center',linespacing=1.45)
c30,s30=np.cos(np.pi/6),np.sin(np.pi/6)
def P(i,j,z): return ((i-j)*c30,(i+j)*s30+z)
def box(ax,i,j,w,d,h,acc,zo):
    faces=[[P(i,j+d,0),P(i,j,0),P(i,j,h),P(i,j+d,h)],[P(i,j,0),P(i+w,j,0),P(i+w,j,h),P(i,j,h)],[P(i,j,h),P(i+w,j,h),P(i+w,j+d,h),P(i,j+d,h)]]
    for poly,c in zip(faces,ISOA if acc else ISO):
        ax.add_patch(Polygon(poly,fc=c,ec=AMB if acc else ISOE,lw=0.6,zorder=zo))
city=[(0,0,1.4,1.4,2.2),(0,2.2,1.2,1.6,3.0),(0,4.6,1.4,1.2,1.6),(2.2,0,1.6,1.2,2.8),(4.6,0,1.2,1.4,1.8),
      (4.6,2.2,1.3,1.3,2.4),(2.0,4.6,1.5,1.3,2.0),(4.4,4.4,1.5,1.5,3.2),(0,6.4,1.0,1.0,1.2),(6.6,0,1.0,1.1,1.4)]
for k,(nm,loss,sub,hl) in enumerate([('분쟁 중앙값',-1.4,'후퇴 1년',0),('하위 25%',-11.0,'피해 큰 4분의 1',0),('우크라이나 2022',-22.7,'후퇴 18년',1),('리비아 2011',-49.1,'후퇴 47년',1)]):
    ax=fig.add_axes([0.045+k*0.11,0.118,0.105,0.115]); ax.axis('off'); ax.set_aspect('equal')
    ax.add_patch(Polygon([P(-0.6,-0.6,0),P(8.2,-0.6,0),P(8.2,8.2,0),P(-0.6,8.2,0)],fc=GROUND,ec=FAINT,lw=0.8))
    items=[(i,j,w,d,h,False) for (i,j,w,d,h) in city]+[(2.5,2.5,1.6,1.6,7.0*(100+loss)/100,True)]
    items.sort(key=lambda q:-(q[0]+q[1]))
    for zz,(i,j,w,d,h,a) in enumerate(items): box(ax,i,j,w,d,h,a,2+zz)
    ref=P(2.5,2.5,7.0)[1]+0.8
    ax.plot([-7.5,7.5],[ref,ref],color=DIM,lw=0.9,ls=(0,(2,2)),zorder=60)
    ax.text(0,ref+1.0,f'{loss:+.1f}%',ha='center',fontsize=15,fontfamily=MONO,color=AMB if hl else FG,zorder=70,fontweight='bold')
    ax.set_xlim(-8,8); ax.set_ylim(-6.2,14.5)
    ax.text(0,-2.8,nm,ha='center',fontsize=13.5,fontweight='bold',color=AMB if hl else FG)
    ax.text(0,-5.2,sub,ha='center',fontsize=12,color=DIM)
T(0.05,0.110,'탑 높이 = 100 + 1인당 GDP 최대 하락률 (점선 = 충격 직전)',fontsize=12.5,color=DIM,va='center')
vr(0.505,0.105,0.385)

# ===== 기능 3 (right) =====
T(0.53,0.378,'기능 3  ·  회복 실패 조기경보 검증',fontsize=19,fontweight='bold',va='center')
T(0.53,0.360,'충격 524건 · 74개국  |  실패 = 3년 뒤 1인당 GDP < 충격 직전 (19.3%)',fontsize=13,color=DIM,va='center')
ax=fig.add_axes([0.72,0.262,0.23,0.070]); style(ax)
mods=[('단순 규칙 · 올해 성장률',0.768),('로지스틱 · 구조',0.743),('로지스틱 · 구조+완충',0.744),('MLP 재설정',0.692),('MLP 기본',0.495)][::-1]
for i,(n,v) in enumerate(mods):
    top=i==4
    ax.barh(i,v-0.45,left=0.45,height=0.14,color=AMB if top else FAINT)
    ax.plot([v],[i],'o',color=AMB if top else FG,ms=8)
    ax.text(v+0.012,i,f'{v:.3f}',va='center',fontsize=13,fontfamily=MONO,color=AMB if top else FG,fontweight='bold' if top else 'normal')
ax.axvline(0.5,color=DIM,lw=0.9,ls=':'); ax.text(0.503,-0.95,'무작위',fontsize=11,color=DIM)
ax.set_yticks(range(5)); ax.set_yticklabels([n for n,_ in mods],fontsize=13.5,color=FG); ax.set_xlim(0.45,0.86); ax.set_xticks([])
T(0.53,0.344,'예측 성능 (AUC)',fontsize=12.5,color=DIM,va='center')
T(0.53,0.244,'올해 성장률 하나가 모든 모델을 이겼다.',fontsize=16,fontweight='bold',va='center')
T(0.53,0.227,'구조·완충 변수, MLP 모두 개선 없음 → 가설 H1·H2 기각',fontsize=13.5,va='center')
T(0.53,0.211,'단, 성장률은 3년 뒤 GDP 경로에 일부 포함된 정보(기계적 관계)',fontsize=12.5,color=DIM,va='center')
ax=fig.add_axes([0.62,0.124,0.33,0.054]); style(ax)
tl=[('군사비',0.260,0.122,True),('원조',0.221,0.164,False),('인플레이션',0.196,0.189,False),('송금',0.181,0.207,False),('투자',0.153,0.233,False)][::-1]
for i,(n,h,l,sig) in enumerate(tl):
    c=AMB if sig else DIM
    ax.plot([l,h],[i,i],color=c,lw=2.6 if sig else 1.2)
    ax.plot([h],[i],'o',color=c,ms=9); ax.plot([l],[i],'o',mfc=BG,mec=c,ms=9,mew=1.6)
    ax.text(max(h,l)+0.01,i,f'{(h-l)*100:+.1f}%p',va='center',fontsize=13,fontfamily=MONO,color=c,fontweight='bold' if sig else 'normal')
ax.set_yticks(range(5)); ax.set_yticklabels([n for n,*_ in tl],fontsize=13.5,color=FG); ax.set_xlim(0.10,0.34); ax.set_xticks([])
T(0.53,0.193,'요인별 실패율   ● 상위 그룹   ○ 하위 그룹',fontsize=12.5,color=DIM,va='center')
T(0.53,0.108,'유의한 차이(국가 단위 부트스트랩 95% CI)는 군사비뿐 (+2.5~+26.7%p), 역인과 가능',fontsize=12.5,color=DIM,va='center')

# ===== 03 기대사항 =====
hr(0.092,c=AMB,lw=2)
label(0.05,0.075,'03','기대사항')
cols=[('피해를 "시간"으로 전달','원조·언론·교육에서 "−22.7%" 대신\n"18년 후퇴"로 설명해 체감도를 높인다.'),
      ('고위험국 우선 선별','충격 직후 성장률만으로 회복 실패 위험\n순위를 매긴다 (AUC 0.77). 복잡한 데이터 불필요.'),
      ('한계와 다음 단계','연관성이며 인과 아님 · 통계 단절국 누락.\n→ 인과 분석, 국가별 후퇴 연수 대시보드로 확장.')]
for k,(h,s) in enumerate(cols):
    x=0.05+k*0.31
    T(x,0.052,h,fontsize=16,fontweight='bold',va='center',color=AMB if k<2 else FG)
    T(x,0.040,s,fontsize=13,va='top',linespacing=1.55)
T(0.95,0.008,'웹: limdongha-7751.github.io/war-setback  |  자료: World Bank WDI · EM-DAT  |  우크라이나 2014년 이후 통계 범위 변경',fontsize=11,color=DIM,ha='right',va='center')
fig.savefig(f'poster_{MODE}.png',dpi=60,facecolor=BG); fig.savefig(f'poster_{MODE}.pdf',facecolor=BG); fig.savefig(f'poster_{MODE}_hi.png',dpi=110,facecolor=BG)
