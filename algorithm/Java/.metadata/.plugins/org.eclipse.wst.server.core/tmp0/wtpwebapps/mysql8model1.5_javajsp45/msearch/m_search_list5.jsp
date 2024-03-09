<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.ResultSet" %>
<%@ page import = "java.sql.SQLException" %>

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
Class.forName("com.mysql.jdbc.Driver");
try{
	String jdbcDriver = "jdbc:mysql://localhost:3306/dev45db?" +
			"useUnicode=true&characterEncoding=euckr";
	String dbUser = "dev45id";
	String dbPass = "dev45pw";
	conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);
	System.out.println(conn + "<-- conn m_search_list.jsp");
//3단계 : 쿼리 실행을 위한 준비 시작	
	if(sk == null && sv == null){
		System.out.println("1-1 sk,sv 둘다 null 조건");
		pstmt = conn.prepareStatement("select * from tb_member");
	}else if(sk != null && sv.equals("")){
		System.out.println("1-2 sk는 null아니고 sv는 공백 조건");
		pstmt = conn.prepareStatement("select * from tb_member");
	}else if(sk != null && sv != null){
		System.out.println("1-3 sk,sv는 null 아닌 조건");
		if(sk.equals("m_id")){
			pstmt = conn.prepareStatement("SELECT * FROM tb_member WHERE m_id=?");
		}else if(sk.equals("m_level")){
			pstmt = conn.prepareStatement("SELECT * FROM tb_member WHERE m_level=?");
		}else if(sk.equals("m_name")){
			pstmt = conn.prepareStatement("SELECT * FROM tb_member WHERE m_name=?");
		}else if(sk.equals("m_email")){
			pstmt = conn.prepareStatement("SELECT * FROM tb_member WHERE m_email=?");
		}
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



