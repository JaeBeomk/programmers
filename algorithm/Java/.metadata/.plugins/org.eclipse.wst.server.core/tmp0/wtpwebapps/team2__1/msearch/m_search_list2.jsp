<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>

<%@ include file="/msearch/m_search_form.jsp" %>
<%
request.setCharacterEncoding("euc-kr");
String sk = request.getParameter("sk");
String sv = request.getParameter("sv");
//3�ܰ� : ���� ���� �غ� �ܰ� : m_list.jsp�� �����ϴ�
System.out.println(sk + "<- sk ");
System.out.println(sv + "<- sv ");
if(sk == null && sv == null){
	System.out.println("1-1 sk,sv �Ѵ� null ����");
	//SELECT * FROM tb_member
}else if(sk != null && sv.equals("")){
	System.out.println("1-2 sk�� null�ƴϰ� sv�� ���� ����");
	//SELECT * FROM tb_member
}else if(sk != null && sv != null){
	System.out.println("1-3 sk,sv�� null �ƴ� ����");
	if(sk.equals("m_id")){
		System.out.println("SELECT * FROM tb_member WHERE m_id='id001' ���� �غ�");
	}else if(sk.equals("m_level")){
		System.out.println("SELECT * FROM tb_member WHERE m_level='�Ǹ���' ���� �غ�");
	}else if(sk.equals("m_name")){
		System.out.println("SELECT * FROM tb_member WHERE m_name='ȫ03' ���� �غ�");
	}else if(sk.equals("m_email")){
		System.out.println("SELECT * FROM tb_member WHERE m_email='test05' ���� �غ�");
	}
}
%>




