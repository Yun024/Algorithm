# [파이썬을 파이썬답게] i번째 원소와 i+1번째 원소

[문제 링크](https://school.programmers.co.kr/learn/courses/4008/lessons/72546) 

### 구분

파이썬을 파이썬답게 > 파트4. Iterable 다루기
### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

<hr>

### 문제설명

<p>숫자를 담은 리스트 mylist가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist의 i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴하도록 코드를 작성해주세요.

단, 마지막에 있는 원소는 (마지막+1)번째의 원소와의 차를 구할 수 없으니, 이 값은 구하지 않습니다.</p>

### 제한 조건

<ul>
<li>mylist의 길이는 1 이상 100 이하인 자연수입니다.</li>
<li>mylist의 원소는 1 이상 100 이하인 자연수입니다.</li>
</ul>

###  예시

<table class="table">
        <thead><tr>
<th>mylist</th>
<th>output</th>
</tr>
</thead>
        <tbody><tr>
<td>[83, 48, 13, 4, 71, 11]</td>
<td>[35, 35, 9, 67, 60]</td>
</tr>
</tbody>
      </table>

### 설명

<p>
<ul>
<li>83과 48의 차는 35입니다.</li>
<li>48과 13의 차는 35입니다.</li>
<li>13과 4의 차는 9입니다.</li>
<li>4와 71의 차는 67입니다.</li>
<li>71과 11의 차는 60입니다.</li>
</ul>
따라서 [35, 35, 9, 67, 60]를 리턴합니다. </p>

<hr>
> 출처: 프로그래머스 파이썬을 파이썬답게, https://school.programmers.co.kr/learn/courses/4008
