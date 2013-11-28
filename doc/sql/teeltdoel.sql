--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: pestileaks_teeltdoel; Type: TABLE; Schema: public; Owner: pestileaks; Tablespace: 
--

CREATE TABLE pestileaks_teeltdoel (
    id integer NOT NULL,
    naam character varying(50) NOT NULL,
    edi_code character varying(10) NOT NULL
);


ALTER TABLE public.pestileaks_teeltdoel OWNER TO pestileaks;

--
-- Data for Name: pestileaks_teeltdoel; Type: TABLE DATA; Schema: public; Owner: pestileaks
--

COPY pestileaks_teeltdoel (id, naam, edi_code) FROM stdin;
1	Friet	1
4	Brouwgerst	101
5	Baktarwe	102
6	Bestrijdingsmaatregel AM	103
7	Bioenergie	104
8	B peen	105
9	Buitenbloemen hoge norm	106
10	Buitenbloemen overig	107
11	C-D peen	108
12	Conserven	109
13	Corncobmix	110
14	Droog te oogsten bonen geen Consumptie	111
15	Droog te oogsten landbouwerwten	112
16	Eenmalige oogst	113
17	Eiwitproductie	114
18	Energiemaïs	115
19	Ensilage	116
20	Faunarand	117
21	Groenbemesting	118
22	Industrie/chips	119
23	Industrie/frites	120
24	Karwijzaad	121
25	Korrelmaïs	122
26	Lijnzaad	123
27	Maaigrasland	124
28	Maalindustrie	125
29	Meermalige oogst	126
30	Natuur maaigrasland	127
31	Natuur met beweiden	128
32	Onderdekkersteelt	129
33	Onderstammen	130
34	Onderteelt	131
35	Onderzetters	132
36	Pennenteelt	133
37	Pootgoed	134
38	Pootgoed ATR	135
39	Pootgoed TBM	136
40	Productie	137
41	Rood	138
42	Schillerij	139
43	Snijderij	140
44	Snijmaïs	141
45	Spillen	142
46	Trekteelt	143
47	Vermeerdering	144
48	Vermeerdering fijnbollige cultivars	145
49	Vermeerdering grofbollige cultivars	146
50	Vermeerdering grote gele cultivars	147
51	Vermeerdering kralen	148
52	Vermeerdering pitten	149
53	Versmarkt	150
54	Vezelindustrie	151
55	Voederindustrie	152
56	Voederteelt	153
57	Wachtbed / vermeerdering	154
58	Weiland	155
59	Wit	156
60	Wortelgewas	157
61	Zaadteelt	158
62	Zetmeel/campagne	159
63	Zetmeel/namalers	160
64	Zetmeel/voormalers	161
65	Zonder opkweek	162
66	Zwart	163
67	Zwarte braak	164
68	Brouwerij	165
69	Industrie	166
70	Bospeen	167
71	Parijse wortelen	168
72	Waspeen	169
73	Wasboon	170
74	Vultarwe	171
75	Sierteelt	172
2	Zetmeel	2
3	Consumptie	3
\.


--
-- PostgreSQL database dump complete
--

SELECT pg_catalog.setval('pestileaks_middel_id_seq', 76, true);
