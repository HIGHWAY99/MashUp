import urllib,urllib2,re,cookielib,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
from universal import watchhistory
    
wh = watchhistory.WatchHistory('plugin.video.movie25')



def iLive():
        main.addDir('All [English]','allenglish',120,art+'/ilive.png')
        main.addDir('Entertainment [English]','entertainmentenglish',120,art+'/ilive.png')
        main.addDir('Sports [English]','sportsenglish',120,art+'/ilive.png')
        main.addDir('All','all',120,art+'/ilive.png')
        main.addDir('General','general',120,art+'/ilive.png')
        main.addDir('Entertainment','entertainment',120,art+'/ilive.png')
        main.addDir('Sports','sports',120,art+'/ilive.png')
        main.addDir('News','news',120,art+'/ilive.png')
        main.addDir('Music','music',120,art+'/ilive.png')
        main.addDir('Animation','animation',120,art+'/ilive.png')
        main.addDir('Family','family',120,art+'/ilive.png')
        ## Seems to be empty atm ##
        main.addDir('Lifecaster (Often Empty)','lifecaster',120,art+'/ilive.png')
        main.addDir('Gaming (Often Empty)','gaming',120,art+'/ilive.png')
        main.addDir('Mobile (Often Empty)','mobile',120,art+'/ilive.png')
        main.addDir('Religion (Often Empty)','religion',120,art+'/ilive.png')
        main.addDir('Radio (Often Empty)','radio',120,art+'/ilive.png')
        main.GA("Live","iLive")
        
def iLiveList(murl):
        if murl=='general':
            try:
                urllist=['http://www.ilive.to/channels/General','http://www.ilive.to/channels/General?p=2']
            except:
                urllist=['http://www.ilive.to/channels/General']
        if murl=='entertainment':
            try:
                urllist=['http://www.ilive.to/channels/Entertainment','http://www.ilive.to/channels/Entertainment?p=2','http://www.ilive.to/channels/Entertainment?p=3','http://www.ilive.to/channels/Entertainment?p=4','http://www.ilive.to/channels/Entertainment?p=5','http://www.ilive.to/channels/Entertainment?p=6']
            except:
                urllist=['http://www.ilive.to/channels/Entertainment','http://www.ilive.to/channels/Entertainment?p=2','http://www.ilive.to/channels/Entertainment?p=3','http://www.ilive.to/channels/Entertainment?p=4','http://www.ilive.to/channels/Entertainment?p=5']
        if murl=='sports':
            try:
                urllist=['http://www.ilive.to/channels/Sport','http://www.ilive.to/channels/Sport?p=2','http://www.ilive.to/channels/Sport?p=3','http://www.ilive.to/channels/Sport?p=4']
            except:
                urllist=['http://www.ilive.to/channels/Sport','http://www.ilive.to/channels/Sport?p=2','http://www.ilive.to/channels/Sport?p=3']
        if murl=='news':
            try:
                urllist=['http://www.ilive.to/channels/News']
            except:
                urllist=['http://www.ilive.to/channels/News']
        if murl=='music':
            try:
                urllist=['http://www.ilive.to/channels/Music']
            except:
                urllist=['http://www.ilive.to/channels/Music']
        if murl=='animation':
            try:
                urllist=['http://www.ilive.to/channels/Animation','http://www.ilive.to/channels/Animation?p=2']
            except:
                urllist=['http://www.ilive.to/channels/Animation']
        if murl=='family':
            try:
                urllist=['http://www.ilive.to/channels/Family']
            except:
                urllist=['http://www.ilive.to/channels/Family']
        if murl=='lifecaster':
            try:
                urllist=['http://www.ilive.to/channels/Lifecaster']
            except:
                urllist=['http://www.ilive.to/channels/Lifecaster']
        if murl=='gaming':
            try:
                urllist=['http://www.ilive.to/channels/Gaming']
            except:
                urllist=['http://www.ilive.to/channels/Gaming']
        if murl=='mobile':
            try:
                urllist=['http://www.ilive.to/channels/Mobile']
            except:
                urllist=['http://www.ilive.to/channels/Mobile']
        if murl=='religion':
            try:
                urllist=['http://www.ilive.to/channels/Religion']
            except:
                urllist=['http://www.ilive.to/channels/Religion']
        if murl=='radio':
            try:
                urllist=['http://www.ilive.to/channels/Radio']
            except:
                urllist=['http://www.ilive.to/channels/Radio']
        if murl=='all':
            try:
                urllist=['http://www.ilive.to/channels','http://www.ilive.to/channels?p=2','http://www.ilive.to/channels?p=3','http://www.ilive.to/channels?p=4','http://www.ilive.to/channels?p=5','http://www.ilive.to/channels?p=6','http://www.ilive.to/channels?p=7','http://www.ilive.to/channels?p=8','http://www.ilive.to/channels?p=9','http://www.ilive.to/channels?p=10','http://www.ilive.to/channels?p=11','http://www.ilive.to/channels?p=12','http://www.ilive.to/channels?p=13','http://www.ilive.to/channels?p=14','http://www.ilive.to/channels?p=15','http://www.ilive.to/channels?p=16']
            except:
                urllist=['http://www.ilive.to/channels','http://www.ilive.to/channels?p=2','http://www.ilive.to/channels?p=3','http://www.ilive.to/channels?p=4','http://www.ilive.to/channels?p=5','http://www.ilive.to/channels?p=6','http://www.ilive.to/channels?p=7','http://www.ilive.to/channels?p=8','http://www.ilive.to/channels?p=9','http://www.ilive.to/channels?p=10']
        if murl=='allenglish':
            try:
                urllist=['http://www.ilive.to/channels?lang=1','http://www.ilive.to/channels?lang=1&p=2','http://www.ilive.to/channels?lang=1&p=3','http://www.ilive.to/channels?lang=1&p=4','http://www.ilive.to/channels?lang=1&p=5','http://www.ilive.to/channels?lang=1&p=6','http://www.ilive.to/channels?lang=1&p=7','http://www.ilive.to/channels?lang=1&p=8','http://www.ilive.to/channels?lang=1&p=9','http://www.ilive.to/channels?lang=1&p=10']
            except:
                urllist=['http://www.ilive.to/channels?lang=1','http://www.ilive.to/channels?lang=1&p=2','http://www.ilive.to/channels?lang=1&p=3','http://www.ilive.to/channels?lang=1&p=4','http://www.ilive.to/channels?lang=1&p=5','http://www.ilive.to/channels?lang=1&p=6','http://www.ilive.to/channels?lang=1&p=7','http://www.ilive.to/channels?lang=1&p=8','http://www.ilive.to/channels?lang=1&p=9']
        if murl=='entertainmentenglish':
            try:
                urllist=['http://www.ilive.to/channels/Entertainment?lang=1','http://www.ilive.to/channels/Entertainment?lang=1&p=2','http://www.ilive.to/channels/Entertainment?lang=1&p=3','http://www.ilive.to/channels/Entertainment?lang=1&p=4','http://www.ilive.to/channels/Entertainment?lang=1&p=5','http://www.ilive.to/channels/Entertainment?lang=1&p=6']
            except:
                urllist=['http://www.ilive.to/channels/Entertainment?lang=1','http://www.ilive.to/channels/Entertainment?lang=1&p=2','http://www.ilive.to/channels/Entertainment?lang=1&p=3','http://www.ilive.to/channels/Entertainment?lang=1&p=4','http://www.ilive.to/channels/Entertainment?lang=1&p=5']
        if murl=='sportsenglish':
            try:
                urllist=['http://www.ilive.to/channels/Sport?lang=1','http://www.ilive.to/channels/Sport?lang=1&p=2']
            except:
                urllist=['http://www.ilive.to/channels/Sport?lang=1']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until channel list is loaded.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading.....[/B]',remaining_display)
        for durl in urllist:
                link=main.OPENURL(durl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('src=".+?" alt=".+?<img width=".+?" height=".+?" src="([^<]+)" alt=".+?"/></noscript></a><a href="(.+?)"><strong>(.+?)</strong></a><br/>.+?<a href="http://[A-Za-z0-9\.]*/channels\?lang=\d*">([A-Za-z]*)</a>').findall(link) #match=re.compile('src=".+?" alt=".+?<img width=".+?" height=".+?" src="([^<]+)" alt=".+?"/></noscript></a><a href="(.+?)"><strong>(.+?)</strong></a><br/>').findall(link)
                for thumb,url,name,lang in match: #for thumb,url,name in match:
                        match=re.compile('Hongkong').findall(name)
                        match2=re.compile('sex').findall(name)
                        if len(match)==0 and len(match2)==0:
                                if name != 'Playboy TV':
                                        main.addPlayL(name+'  ['+lang+']',url,121,thumb,'','','','','') #main.addPlayL(name,url,121,thumb,'','','','','')
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading.....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("iLive","List") 

def getToken(url):
        from t0mm0.common.net import Net
        net = Net()
        html = net.http_GET(url).content
        token_url = re.compile('\$.getJSON\("(.+?)",').findall(html)[0]

        import datetime
        time_now=datetime.datetime.now()
        import time
        epoch=time.mktime(time_now.timetuple())+(time_now.microsecond/1000000.)
        epoch_str = str('%f' % epoch)
        epoch_str = epoch_str.replace('.','')
        epoch_str = epoch_str[:-3]

        token_url = token_url + '&_=' + epoch_str
        token = re.compile('":"(.+?)"').findall(net.http_GET(token_url+'&_='+str(epoch), headers={'Referer':url}).content)[0]
        return token

def iLiveLink(mname,murl,thumb):
        main.GA("iLive","Watched")
        stream_url=False
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Stream,3000)")
        link=main.OPENURL(murl)
        ok=True
        if link:
                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playlist.clear()
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('http://www.ilive.to/embed/(.+?)&width=(.+?)&height=(.+?)&autoplay=true').findall(link)
                for fid,wid,hei in match:
                    pageUrl='http://www.ilive.to/embedplayer.php?width='+wid+'&height='+hei+'&channel='+fid+'&autoplay=true'
                link=main.OPENURL(pageUrl)
                playpath=re.compile('file: "(.+?).flv"').findall(link)
                token=getToken(pageUrl)
                if len(playpath)==0:
                        playpath=re.compile('http://snapshots.ilive.to/snapshots/(.+?)_snapshot.jpg').findall(thumb)      
                for playPath in playpath:
                    stream_url = 'rtmp://live.iguide.to/edge playpath=' + playPath + " live=1 timeout=15 swfUrl=http://player.ilive.to/player_ilive_2.swf pageUrl="+pageUrl+" token="+token
                listitem = xbmcgui.ListItem(thumbnailImage=thumb)
                listitem.setInfo('video', {'Title': mname, 'Genre': 'Live'} )
        
                playlist.add(stream_url,listitem)
                xbmcPlayer = xbmc.Player()
                xbmcPlayer.play(playlist)
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    wh.add_item(mname+' '+'[COLOR green]iLive[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                return ok

