# Reference Evidence Interpreter Cases

Status: Pre-Implementation Test Matrix

| Case | Evidence | Profile state | Expected path | primary evidence unit | token contributions considered? | expected winning identity | expected statistics_available | expected statistical_coverage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RI001 | exact SB8891 | frequency 1/100 | normalized reference | normalized reference | no | sb8891 | true | 1.0 |
| RI002 | exact CREDITNOTE | frequency 80/100 | normalized reference | normalized reference | no | creditnote | true | 1.0 |
| RI003 | exact NEW999999 | unavailable | normalized reference fallback | normalized reference | no | new999999 | false | 0.0 |
| RI004 | shared 874219 | DF 1/100 | token | token | yes | 874219 | true | 1.0 |
| RI005 | shared 001 | DF 80/100 | token | token | yes | 001 | true | 1.0 |
| RI006 | shared 874219 | unavailable | long token fallback | token | yes | 874219 | false | 0.0 |
| RI007 | shared 001 | unavailable | medium repeated-pattern fallback | token | yes | 001 | false | 0.0 |
| RI008 | shared 01 | unavailable | short repeated-pattern fallback | token | yes | 01 | false | 0.0 |
| RI009 | shared 000000 | unavailable | long repeated-pattern fallback | token | yes | 000000 | false | 0.0 |
| RI010 | tokens 2026, 874219 | DF 80/100, 1/100 | strongest token | token | yes | 874219 | true | 1.0 |
| RI011 | tokens 991827, 874219 | DF 1/100, 1/100 | deterministic tie | token | yes | 874219 | true | 1.0 |
| RI012 | token A fallback 0.60, token B profiled 0.55 | mixed | fallback winner | token | yes | token A | false | 0.0 |
| RI013 | token A fallback 0.40, token B profiled 0.55 | mixed | profiled winner | token | yes | token B | true | 1.0 |
| RI014 | token A fallback 0.60, token B profiled 0.60 | mixed | profiled tie winner | token | yes | token B | true | 1.0 |
| RI015 | exact reference with numeric substring | profiled | exact path only | normalized reference | no | exact normalized match | true | 1.0 |

For RI015 explicitly state: exact normalized identity exists -> shared numeric token is not interpreted. This prevents double counting.
