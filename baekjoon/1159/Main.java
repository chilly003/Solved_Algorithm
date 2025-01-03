import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        // 파일에서 입력을 읽어오기 위한 설정
        FileReader fileReader = new FileReader("1159.txt"); // 파일 읽기
        BufferedReader bufferedReader = new BufferedReader(fileReader); // 파일 내용을 효율적으로 읽기 위한 BufferedReader

        // 알파벳 개수를 저장할 배열 (a-z: 총 26개)
        int[] alphabet = new int[26]; // 각 알파벳의 첫 글자 개수를 저장할 배열
        StringBuilder answer = new StringBuilder(); // 결과를 저장할 문자열

        // 첫 번째 줄에서 테스트 케이스 개수를 읽어옴
        String firstLine = bufferedReader.readLine(); // 파일의 첫 줄 읽기
        int T = Integer.parseInt(firstLine); // 테스트 케이스 개수로 변환

        // 테스트 케이스만큼 반복해서 이름을 읽음
        for (int i = 0; i < T; i++) {
            String firstName = bufferedReader.readLine(); // 한 줄씩 이름을 읽음
            char firstChar = firstName.charAt(0); // 이름의 첫 글자를 가져옴
            int index = firstChar - 'a'; // 'a'를 기준으로 몇 번째 알파벳인지 계산 (예: 'a'는 0, 'b'는 1)
            alphabet[index]++; // 해당 알파벳의 개수를 증가시킴
        }

        // 알파벳 배열에서 조건 확인 (5명 이상인 알파벳 찾기)
        for (int i = 0; i < 26; i++) { // a부터 z까지 반복
            if (alphabet[i] >= 5) {   // 해당 알파벳의 개수가 5 이상이면
                char letter = (char) (i + 'a'); // 인덱스를 문자로 변환 ('a'부터 시작)
                answer.append(letter);         // 결과 문자열에 추가
            }
        }

        // 결과 출력
        if (answer.length() > 0) { // 결과 문자열이 비어 있지 않으면
            System.out.println(answer.toString()); // 결과 출력
        } else { // 결과 문자열이 비어 있으면
            System.out.println("PREDAJA"); // "PREDAJA" 출력
        }

        bufferedReader.close(); // 파일 닫기
    }
}