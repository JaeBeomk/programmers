<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%
System.out.println(session + "<- session top.jsp");
System.out.println(request + "<- request top.jsp");
System.out.println(response + "<- response top.jsp");
System.out.println(out + "<- out top.jsp");
String S_ID = (String)session.getAttribute("S_ID");
String S_NAME = (String)session.getAttribute("S_NAME");
String S_LEVEL = (String)session.getAttribute("S_LEVEL");
System.out.println(S_ID + "<- S_ID top.jsp");
System.out.println(S_NAME + "<- S_NAME top.jsp");
System.out.println(S_LEVEL + "<- S_LEVEL top.jsp");
%>
   <!-- Begin Wrapper -->
   <div id="wrapper">
   
         <!-- Begin Header -->
         <div id="header">
         /module/top.jsp	<br/>
		       상단 메뉴	<br/><br/>
<%
if(S_LEVEL == null){
%>		
<!-- 1 로그인 전 화면 시작 -->	
<a href="<%= request.getContextPath() %>/minsert/m_insert_form.jsp">01회원등록</a><br/>	       		 
<form action="<%= request.getContextPath() %>/login/login_action.jsp" method="post">
	아이디:	<input type="text" name="id">
	비번 : <input type="text" name="pw">
	<input type="submit" value="로그인버튼"> 
</form> 
<!-- 1 로그인 전 화면 끝 -->
<%
}else{
	if(S_LEVEL.equals("구매자")){
%>		
<a href="<%= request.getContextPath() %>/minsert/m_insert_form.jsp">01회원등록</a>
<a href="#">04상품검색</a>	<br/>	
<%		
	}else if(S_LEVEL.equals("판매자")){
%>		
<a href="<%= request.getContextPath() %>/minsert/m_insert_form.jsp">01회원등록</a>
<a href="<%= request.getContextPath() %>/mginsert/goods_insert_form2.jsp">03상품등록</a>
<a href="<%= request.getContextPath() %>/mgsearch/mg_search_list1.jsp">04상품검색</a>		
<a href="<%= request.getContextPath() %>/mgsearch/mg_search_list1.jsp">05상품회원join검색1</a>	<br/>	
<%		
	}else if(S_LEVEL.equals("관리자")){
%>		
<a href="<%= request.getContextPath() %>/minsert/m_insert_form.jsp">01회원등록</a>
<a href="<%= request.getContextPath() %>/msearch/m_search_list.jsp">02회원검색</a>
<a href="<%= request.getContextPath() %>/mginsert/goods_insert_form2.jsp">03상품등록</a>
<a href="<%= request.getContextPath() %>/mgsearch/mg_search_list1.jsp">04상품검색</a>	
<a href="<%= request.getContextPath() %>/mgsearch/mg_search_list1.jsp">05상품회원join검색1</a>	<br/>	

<%		
	}
%>
<!-- 2 로그인 후 화면 시작 -->
	<%= S_NAME %> 님 <%= S_LEVEL %> 권한 로그인 상태
<a href="<%= request.getContextPath() %>/login/logout.jsp">로그아웃</a>
<!-- 2 로그인 후 화면 끝 -->
<%
}
%>			   
		 </div>
		 <!-- End Header -->