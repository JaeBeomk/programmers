-- 상위 n개 레코드
-- 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문
-- MIN(A) = 가장 옛날값
-- MAX(A) = 가장 최근값
SELECT
    NAME
FROM
    ANIMAL_INS
WHERE DATETIME =(
                SELECT 
                    MIN(DATETIME) 
                FROM
                    ANIMAL_INS
                );
                    
