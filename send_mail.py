def send_mail(toaddrs='2606680127@vtext.com',msg='An error has occurred!'):
    import smtplib
    
    fromaddr = 'sentherus@gmail.com'
    
    
    # Credentials (if needed)
    username = 'sentherus@gmail.com'
    password = 'ksbpmkguekqislcc'
    
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

