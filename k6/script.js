import http from 'k6/http';
import { sleep } from 'k6';
export const options = {
    scenarios: {
        common_scenario: {
            executor: 'constant-vus',
            exec: 'test',
            vus: 100,
            duration: '12s',
            startTime: '2s',
        }
    }
};

export function test () {
  http.get('https://web/django/workload/prime-number');
}