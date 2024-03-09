<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>

<%@ include file="/msearch/m_search_form.jsp" %>
<%
request.setCharacterEncoding("euc-kr");
String sk = request.getParameter("sk");
String sv = request.getParameter("sv");
//3단계 : 쿼리 실행 준비 단계 : m_list.jsp와 동일하다
System.out.println(sk + "<- sk ");
System.out.println(sv + "<- sv ");
if(sk == null && sv == null){
	System.out.println("1-1 sk,sv 둘다 null 조건");
	//SELECT * FROM tb_member
}else if(sk != null && sv.equals("")){
	System.out.println("1-2 sk는 null아니고 sv는 공백 조건");
	//SELECT * FROM tb_member
}else if(sk != null && sv != null){
	System.out.println("1-3 sk,sv는 null 아닌 조건");
	if(sk.equals("m_id")){
		System.out.println("SELECT * FROM tb_member WHERE m_id='id001' 쿼리 준비");
	}else if(sk.equals("m_level")){
		System.out.println("SELECT * FROM tb_member WHERE m_level='판매자' 쿼리 준비");
	}else if(sk.equals("m_name")){
		System.out.println("SELECT * FROM tb_member WHERE m_name='홍03' 쿼리 준비");
	}else if(sk.equals("m_email")){
		System.out.println("SELECT * FROM tb_member WHERE m_email='test05' 쿼리 준비");
	}
}
%>




