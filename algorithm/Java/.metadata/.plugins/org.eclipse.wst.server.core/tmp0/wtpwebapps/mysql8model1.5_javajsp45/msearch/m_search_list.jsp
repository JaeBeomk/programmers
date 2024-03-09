<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.ResultSet" %>
<%@ page import = "java.sql.SQLException" %>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>

<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<!-- 상대경로 방법 -->
<!-- <link rel="stylesheet" type="text/css" href="./css/main.css" /> -->
<!-- 절대경로 방법1 : 문제점 : 프로젝트명 변경되면 망했다. 왜? 관련 1억개 파일 변경 -->
<!-- <link rel="stylesheet" type="text/css" href="/layoutMG45/css/main.css" /> -->
<!-- 절대경로 방법2 -->
<link rel="stylesheet" type="text/css" href="<%= request.getContextPath() %>/css/main.css" />
</head>
<body>
<%@ include file="/module/top.jsp" %>
<%@ include file="/module/left.jsp" %>
<%@ include file="/msearch/m_search_form.jsp" %>
회원 검색 <br>
<table width="100%" border="1">
<tr>
	<td>아이디</td><td>비번</td><td>권한</td><td>이름</td><td>이메일</td><td>수정</td><td>삭제</td>
</tr>
<%
request.setCharacterEncoding("euc-kr");
String sk = request.getParameter("sk");
String sv = request.getParameter("sv");
//3단계 : 쿼리 실행 준비 단계 : m_list.jsp와 동일하다

Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;
try{
	DriverDB db = new DriverDB();
	conn = db.driverDbcon();
	System.out.println(conn + "<-- conn m_search_list.jsp");
//3단계 : 쿼리 실행을 위한 준비 시작
	String selectQuery="select * from tb_member";
	if(sk == null && sv == null){
		System.out.println("1-1 sk,sv 둘다 null 조건");
		pstmt = conn.prepareStatement(selectQuery);
	}else if(sk != null && sv.equals("")){
		System.out.println("1-2 sk는 null아니고 sv는 공백 조건");
		pstmt = conn.prepareStatement(selectQuery);
	}else if(sk != null && sv != null){
		System.out.println("1-3 sk,sv는 null 아닌 조건");
		pstmt = conn.prepareStatement(selectQuery+" WHERE "+sk+"=?");
		pstmt.setString(1, sv);
	}
	System.out.println(pstmt + "<-- pstmt");
//3단계 : 쿼리 실행을 위한 준비 끝	
	rs = pstmt.executeQuery();
	System.out.println(rs + "<-- rs m_search_list.jsp");
	while(rs.next()){
		System.out.println("while 반복 횟수");
%>		
		<tr>
			<td><%= rs.getString("m_id")%></td>
			<td><%= rs.getString("m_pw")%></td>
			<td><%= rs.getString("m_level")%></td>
			<td><%= rs.getString("m_name")%></td>
			<td><%= rs.getString("m_email")%></td>
			<td>
<a href="<%= request.getContextPath() %>/mupdate/m_update_form.jsp?m_id=<%= rs.getString("m_id")%>">수정클릭</a>			
			</td>
			<td>
<a href="<%= request.getContextPath() %>/mdelete/m_delete_action.jsp?m_id=<%= rs.getString("m_id")%>">삭제클릭</a>			
			</td>
		</tr>	
<%		
	}
} catch(SQLException ex) {
	out.println(ex.getMessage());
	ex.printStackTrace();
} finally {
	// 6. 사용한 Statement 종료
	if (rs != null) try { rs.close(); } catch(SQLException ex) {}
	if (pstmt != null) try { pstmt.close(); } catch(SQLException ex) {}
	
	// 7. 커넥션 종료
	if (conn != null) try { conn.close(); } catch(SQLException ex) {}
}
%>
</table>
<%@ include file="/module/hadan.jsp" %>
</body>
</html>


