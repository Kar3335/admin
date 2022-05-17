#Created for coded32 and his teamopenfire Eliminated Some bugs from my last code shared here as Guest.<br />
#Greets To T.O.F and Indishell<br />
#Thanks friends for find bugs and give suggetions<br />
<br />
#cd direcory/to/code<br />
#direcory/to/code>python code.py<br />
<br />
#improved Error Handling<br />
#Find out usefull stuffs from www.teamopenfire.com<br />
#"wE aRe gREat inDIans"<br />
<br />
import httplib<br />
import socket<br />
import sys<br />
<br />
<br />
try:<br />
print "\t################################################################"<br />
print "\t#                                        www.teamopenfire.com  #"<br />
print "\t#       ###############      ########       ############       #"<br />
print "\t#       #             #     ##      ##      #          #       #"<br />
print "\t#       ######   ######     ##      ##      #   ########       #"<br />
print "\t#            #   #          ##      ##      #   #              #"<br />
print "\t#            #   #          ##      ##      #   #####          #"<br />
print "\t#            #   #          ##      ##      #   #####          #"<br />
print "\t#            #   #          ##      ##      #   #              #"<br />
print "\t#            #   #          ##      ##      #   #              #"<br />
print "\t#            #####    [#]    ########   [#] #####  AdminFinder #"<br />
print "\t#                                                              #"<br />
print "\t#                                            coded by Ajith KP #"<br />
print "\t#                          Greets to Coded32 and T.O.F members #"<br />
print "\t################################################################"<br />
var1=0<br />
var2=0<br />
<br />
php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',<br />
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',<br />
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',<br />
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',<br />
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',<br />
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',<br />
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',<br />
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',<br />
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',<br />
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',<br />
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',<br />
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',<br />
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',<br />
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',<br />
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',<br />
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',<br />
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',<br />
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',<br />
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']<br />
<br />
asp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',<br />
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',<br />
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',<br />
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',<br />
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',<br />
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',<br />
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',<br />
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',<br />
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',<br />
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',<br />
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',<br />
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',<br />
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',<br />
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',<br />
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',<br />
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',<br />
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',<br />
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',<br />
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html']<br />
<br />
cfm = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',<br />
'memberadmin/','administratorlogin/','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',<br />
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',<br />
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',<br />
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',<br />
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',<br />
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',<br />
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',<br />
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',<br />
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',<br />
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',<br />
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',<br />
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',<br />
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',<br />
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',<br />
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',<br />
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',<br />
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',<br />
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm']<br />
<br />
js = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',<br />
'memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',<br />
'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',<br />
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',<br />
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',<br />
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',<br />
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',<br />
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',<br />
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',<br />
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',<br />
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',<br />
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',<br />
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',<br />
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',<br />
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',<br />
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',<br />
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',<br />
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',<br />
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js']<br />
<br />
cgi = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',<br />
'memberadmin/','administratorlogin/','adm/','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi','admin/account.cgi',<br />
'admin_area/admin.cgi','admin_area/login.cgi','siteadmin/login.cgi','siteadmin/index.cgi','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',<br />
'admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',<br />
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',<br />
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',<br />
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',<br />
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',<br />
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',<br />
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',<br />
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',<br />
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',<br />
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',<br />
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',<br />
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',<br />
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',<br />
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',<br />
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',<br />
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi']<br />
<br />
brf = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',<br />
'memberadmin/','administratorlogin/','adm/','admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf',<br />
'admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',<br />
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',<br />
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',<br />
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',<br />
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',<br />
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',<br />
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',<br />
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',<br />
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',<br />
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',<br />
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',<br />
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',<br />
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',<br />
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',<br />
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',<br />
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',<br />
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf']<br />
<br />
try:<br />
site = raw_input("Web Site for Scan?: ")<br />
site = site.replace("http://","")<br />
print ("\tChecking website " + site + "...")<br />
conn = httplib.HTTPConnection(site)<br />
conn.connect()<br />
print "\t[$] Yes... Server is Online."<br />
except (httplib.HTTPResponse, socket.error) as Exit:<br />
raw_input("\t [!] Oops Error occured, Server offline or invalid URL")<br />
exit()<br />
print "Enter site source code:"<br />
print "1 PHP"<br />
print "2 ASP"<br />
print "3 CFM"<br />
print "4 JS"<br />
print "5 CGI"<br />
print "6 BRF"<br />
print "\nPress 1 and 'Enter key' for Select PHP\n"<br />
code=input("> ")<br />
<br />
if code==1:<br />
print("\t [+] Scanning " + site + "...\n\n")<br />
for admin in php:<br />
admin = admin.replace("\n","")<br />
admin = "/" + admin<br />
host = site + admin<br />
print ("\t [#] Checking " + host + "...")<br />
connection = httplib.HTTPConnection(site)<br />
connection.request("GET",admin)<br />
response = connection.getresponse()<br />
var2 = var2 + 1<br />
if response.status == 200:<br />
var1 = var1 + 1<br />
print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")<br />
raw_input("Press enter to continue scanning.\n")<br />
elif response.status == 404:<br />
var2 = var2<br />
elif response.status == 302:<br />
print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")<br />
else:<br />
print "%s %s %s" % (host, " Interesting response:", response.status)<br />
connection.close()<br />
print("\n\nCompleted \n")<br />
print var1, " Admin pages found"<br />
print var2, " total pages scanned"<br />
raw_input("[/] The Game Over; Press Enter to Exit")<br />
<br />
<br />
if code==2:<br />
print("\t [+] Scanning " + site + "...\n\n")<br />
for admin in asp:<br />
admin = admin.replace("\n","")<br />
admin = "/" + admin<br />
host = site + admin<br />
print ("\t [#] Checking " + host + "...")<br />
connection = httplib.HTTPConnection(site)<br />
connection.request("GET",admin)<br />
response = connection.getresponse()<br />
var2 = var2 + 1<br />
if response.status == 200:<br />
var1 = var1 + 1<br />
print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")<br />
raw_input("Press enter to continue scanning.\n")<br />
elif response.status == 404:<br />
var2 = var2<br />
elif response.status == 302:<br />
print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")<br />
else:<br />
print "%s %s %s" % (host, " Interesting response:", response.status)<br />
connection.close()<br />
print("\n\nCompleted \n")<br />
print var1, " Admin pages found"<br />
print var2, " total pages scanned"<br />
raw_input("The Game Over; Press Enter to Exit")<br />
<br />
if code==3:<br />
print("\t [+] Scanning " + site + "...\n\n")<br />
for admin in cfm:<br />
admin = admin.replace("\n","")<br />
admin = "/" + admin<br />
host = site + admin<br />
print ("\t [#] Checking " + host + "...")<br />
connection = httplib.HTTPConnection(site)<br />
connection.request("GET",admin)<br />
response = connection.getresponse()<br />
var2 = var2 + 1<br />
if response.status == 200:<br />
var1 = var1 + 1<br />
print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")<br />
raw_input("Press enter to continue scanning.\n")<br />
elif response.status == 404:<br />
var2 = var2<br />
elif response.status == 302:<br />
print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")<br />
else:<br />
print "%s %s %s" % (host, " Interesting response:", response.status)<br />
connection.close()<br />
print("\n\nCompleted \n")<br />
print var1, " Admin pages found"<br />
print var2, " total pages scanned"<br />
raw_input("The Game Over; Press Enter to Exit")<br />
<br />
if code==4:<br />
print("\t [+] Scanning " + site + "...\n\n")<br />
for admin in js:<br />
admin = admin.replace("\n","")<br />
admin = "/" + admin<br />
host = site + admin<br />
print ("\t [#] Checking " + host + "...")<br />
connection = httplib.HTTPConnection(site)<br />
connection.request("GET",admin)<br />
response = connection.getresponse()<br />
var2 = var2 + 1<br />
if response.status == 200:<br />
var1 = var1 + 1<br />
print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")<br />
raw_input("Press enter to continue scanning.\n")<br />
elif response.status == 404:<br />
var2 = var2<br />
elif response.status == 302:<br />
print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")<br />
else:<br />
print "%s %s %s" % (host, " Interesting response:", response.status)<br />
connection.close()<br />
print("\n\nCompleted \n")<br />
print var1, " Admin pages found"<br />
print var2, " total pages scanned"<br />
raw_input("The Game Over; Press Enter to Exit")<br />
<br />
if code==5:<br />
print("\t [+] Scanning " + site + "...\n\n")<br />
for admin in cgi:<br />
admin = admin.replace("\n","")<br />
admin = "/" + admin<br />
host = site + admin<br />
print ("\t [#] Checking " + host + "...")<br />
connection = httplib.HTTPConnection(site)<br />
connection.request("GET",admin)<br />
response = connection.getresponse()<br />
var2 = var2 + 1<br />
if response.status == 200:<br />
var1 = var1 + 1<br />
print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")<br />
raw_input("Press enter to continue scanning.\n")<br />
elif response.status == 404:<br />
var2 = var2<br />
elif response.status == 302:<br />
print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")<br />
else:<br />
print "%s %s %s" % (host, " Interesting response:", response.status)<br />
connection.close()<br />
print("\n\nCompleted \n")<br />
print var1, " Admin pages found"<br />
print var2, " total pages scanned"<br />
raw_input("The Game Over; Press Enter to Exit")<br />
<br />
if code==6:<br />
print("\t [+] Scanning " + site + "...\n\n")<br />
for admin in brf:<br />
admin = admin.replace("\n","")<br />
admin = "/" + admin<br />
host = site + admin<br />
print ("\t [#] Checking " + host + "...")<br />
connection = httplib.HTTPConnection(site)<br />
connection.request("GET",admin)<br />
response = connection.getresponse()<br />
var2 = var2 + 1<br />
if response.status == 200:<br />
var1 = var1 + 1<br />
print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")<br />
raw_input("Press enter to continue scanning.\n")<br />
elif response.status == 404:<br />
var2 = var2<br />
elif response.status == 302:<br />
print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")<br />
else:<br />
print "%s %s %s" % (host, " Interesting response:", response.status)<br />
connection.close()<br />
print("\n\nCompleted \n")<br />
print var1, " Admin pages found"<br />
print var2, " total pages scanned"<br />
raw_input("The Game Over; Press Enter to Exit")<br />
except (httplib.HTTPResponse, socket.error):<br />
print "\n\t[!] Session Cancelled; Error occured. Check internet settings"<br />
except (KeyboardInterrupt, SystemExit):<br />
print "\n\t[!] Session cancelled"<br />
<br />
