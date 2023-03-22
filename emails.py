def send_email_verified(email,token,pk,name):
    import smtplib 
    import requests
    import json
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    remitente = 'evansoft.test@gmail.com'
    destinatarios = ["granmaestroismaelsantana@gmail.com",str(email)]
    asunto = 'Validación de cuenta'
    html = """\
			<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
			<html xmlns="http://www.w3.org/1999/xhtml">
			<head>
			  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
			  <title>Factura electronica</title>
			  <style type="text/css">
				  body {margin: 0; padding: 0; min-width: 100%!important;}
				  img {height: auto;}
				  .content {width: 100%; max-width: 600px;}
				  .header {padding: 40px 30px 20px 30px;}
				  .innerpadding {padding: 30px 30px 30px 30px;}
				  .borderbottom {border-bottom: 1px solid #f2eeed;}
				  .subhead {font-size: 15px; color: #ffffff; font-family: sans-serif; letter-spacing: 10px;}
				  .h1, .h2, .bodycopy {color: #153643; font-family: sans-serif;}
				  .h1 {font-size: 33px; line-height: 38px; font-weight: bold;}
				  .h2 {padding: 0 0 15px 0; font-size: 24px; line-height: 28px; font-weight: bold;}
				  .bodycopy {font-size: 16px; line-height: 22px;}
				  .button {text-align: center; font-size: 18px; font-family: sans-serif; font-weight: bold; padding: 0 30px 0 30px;}
				  .button a {color: #ffffff; text-decoration: none;}
				  .footer {padding: 20px 30px 15px 30px;}
				  .footercopy {font-family: sans-serif; font-size: 14px; color: #ffffff;}
				  .footercopy a {color: #ffffff; text-decoration: underline;}
				  @media only screen and (max-width: 550px), screen and (max-device-width: 550px) {
				  body[yahoo] .hide {display: none!important;}
				  body[yahoo] .buttonwrapper {background-color: transparent!important;}
				  body[yahoo] .button {padding: 0px!important;}
				  body[yahoo] .button a {background-color: #e05443; padding: 15px 15px 13px!important;}
				  body[yahoo] .unsubscribe {display: block; margin-top: 20px; padding: 10px 50px; background: #2f3942; border-radius: 5px; text-decoration: none!important; font-weight: bold;}
			  }
			  </style>
			</head>
			<body yahoo bgcolor="#f6f8f1">
			<table width="100%" bgcolor="#f6f8f1" border="0" cellpadding="0" cellspacing="0">
			<tr>
			  <td>
			    <!--[if (gte mso 9)|(IE)]>
			      <table width="600" align="center" cellpadding="0" cellspacing="0" border="0">
			        <tr>
			          <td>
			    <![endif]-->     
			    <table bgcolor="#ffffff" class="content" align="center" cellpadding="0" cellspacing="0" border="0">
			      <tr>
			        <td style=" background-image: linear-gradient(to left top, #0db9f8, #0790be, #0c6988, #0f4456, #0c222a);" class="header">
			          <table width="100" align="left" border="0" cellpadding="0" cellspacing="0">  
			            <tr>
			              <td height="70" style="padding: 0 20px 20px 0;">
			                <img class="fix" src="http://evansoft.pythonanywhere.com/static/logo.png" style="width:100%; heigth:100%;" border="0" alt="" />
			              </td>
			            </tr>
			          </table>
			          <!--[if (gte mso 9)|(IE)]>
			            <table width="425" align="left" cellpadding="0" cellspacing="0" border="0">
			              <tr>
			                <td>
			          <![endif]-->
			          <table class="col425" align="left" border="0" cellpadding="0" cellspacing="0" style="width: 100%; max-width: 425px;">  
			            <tr>
			              <td height="70">
			                <table width="100%" border="0" cellspacing="0" cellpadding="0">
			                  <tr>
			                    <td class="h1" style="padding: 5px 0 0 0;">
			                     <span style="color: white;">Bienvenida a Evansoft</span>
			                    </td>
			                  </tr>
			                </table>
			              </td>
			            </tr>
			          </table>
			          <!--[if (gte mso 9)|(IE)]>
			                </td>
			              </tr>
			          </table>
			          <![endif]-->
			        </td>
			      </tr>
			      <tr>
			        <td class="innerpadding borderbottom">
			          <table width="100%" border="0" cellspacing="0" cellpadding="0">
			            <tr>
			              <td class="h2">
			               Hola,$(name) !
			              </td>
			            </tr>
			            <tr>
			              <td class="bodycopy">Correo de activación de cuenta y validación de datos
			              </td>
			            </tr>
			          </table>
			        </td>
			      </tr>
			      <tr>
			        <td class="innerpadding borderbottom">
			          <!--[if (gte mso 9)|(IE)]>
			            <table width="380" align="left" cellpadding="0" cellspacing="0" border="0">
			              <tr>
			                <td>
			          <![endif]-->
			          <table class="col380" align="left" border="0" cellpadding="0" cellspacing="0" style="width: 100%; max-width: 380px;">  
			            <tr>
			              <td>
			                <table width="100%" border="0" cellspacing="0" cellpadding="0">
			               
			                  <tr>
			                    <td style="padding: 20px 0 0 0;">
			                      <table class="buttonwrapper" style="background-image: linear-gradient(to left bottom, #0db9f8, #0790be, #0c6988, #0f4456, #0c222a);" border="0" cellspacing="0" cellpadding="0">
			                        <tr>
			                          <td class="button" height="45">
			                            <a href="http://localhost:8000/user/Verified_Activate/$(token)/$(pk)/" target="_blank">Verificar</a>
			                          </td>
			                        </tr>
			                        </tr>
			                      </table>
			                    </td>
			                  </tr>
			                </table>
			              </td>
			            </tr>
			          </table>
			          <!--[if (gte mso 9)|(IE)]>
			                </td>
			              </tr>
			          </table>
			          <![endif]-->
			        </td>
			      </tr>
			    </table>
			    <!--[if (gte mso 9)|(IE)]>
			          </td>
			        </tr>
			    </table>
			    <![endif]-->
			    </td>
			  </tr>
			</table>
			</body>
			</html>
    """
    html = html.replace("$(token)",str(token))
    html = html.replace("$(pk)",str(pk))
    html = html.replace("$(name)",str(name))
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(html,'html'))
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    usuario = "evansoftservices@gmail.com"
    clave = "xarauthaynkevvpj"
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    texto = mensaje.as_string()
    remitente = usuario
    sesion_smtp.login(usuario,clave)
    sesion_smtp.sendmail(remitente, destinatarios, texto)
    sesion_smtp.quit()