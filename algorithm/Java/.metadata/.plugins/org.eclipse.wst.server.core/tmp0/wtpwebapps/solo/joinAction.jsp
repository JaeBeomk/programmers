<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@page import="java.io.PrintWriter"%>
<%@page import="dao.Udao"%>
<%@page import="dto.User"%>
<%request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="user" class="dto.User" scope="page"/>
<jsp:setProperty name="user" property="userID"/>
<jsp:setProperty name="user" property="userPassword"/>
<jsp:setProperty name="user" property="userName"/>
<jsp:setProperty name="user" property="userGender"/>
<jsp:setProperty name="user" property="userEmail"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>�α��� �׼ǰ���</title>
</head>
<body>
	<% 
	//���� ���� ���� üũ
		String userID=null;
		if(session.getAttribute("userID")!=null){
			userID=(String)session.getAttribute("userID");
		}
		//�α��� ������ ȸ�������� �Ұ��� �ϰ�
		if(userID !=null){
			PrintWriter script=response.getWriter();
			script.println("<script>");
			script.println("alert('�̹� �α��� �Ǿ����ϴ�')");
			script.println("location.href='main.jsp'");
			script.println("</script>");
		}
	if(user.getUserID() == null || user.getUserPassword()==null || user.getUserName()==null|| user.getUserGender() == null || user.getUserEmail()==null){
		PrintWriter script=response.getWriter();
		script.println("<script>");
		script.println("alert('�ʼ� �Է� �����Դϴ�.')");
		script.println("</script>");
	}else{
		Udao udao = new Udao();
		int result=udao.join(user);
		if(result==-1){
			PrintWriter script=response.getWriter();
			script.println("<script>");
			script.println("alert('�̹� �����ϴ� ���̵� �Դϴ�.')");
			script.println("history.back()");
			
			script.println("</script>");
		}else{
			session.setAttribute("userID", user.getUserID());
			PrintWriter script=response.getWriter();
			script.println("<script>");
			script.println("alert('ȸ������ ����')");
			script.println("location.href='main.jsp'");
			
			script.println("</script>");
		}
		
	}
	%>
</body>
</html>