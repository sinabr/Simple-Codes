alpha [A-Za-z]
digit [0-9]
%option noyywrap
%{
	#include<stdio.h>
	#include<stdlib.h>
	#define IF (20);
	#define NUM (23);
	#define ID (24);
	#define LE (25);
	#define GE (26);
	#define EQ (27);
	#define NE (28);
	#define OR (29);
	#define AND (30);
	#define WHILE (31);
	#define FOR (32);
	#define ASSIGN (33);
	#define SUM (34);
	#define SUB (35);
	#define MUL (36);
	#define DIV (37);
	#define RELOP (38);
%}

%%
[ \t\n]
if    						{printf("%s\n",yytext);return IF;};
while 						{printf("%s\n",yytext);return WHILE;};
for 						{printf("%s\n",yytext);return FOR;};
{digit}+    					{printf("%s\n",yytext);return  NUM;}
{alpha}({alpha}|{digit})*    			{printf("%s\n",yytext);return  ID;}
"<="    					{printf("%s\n",yytext); LE;return RELOP;}
">="    					{printf("%s\n",yytext); GE;return RELOP;}
"=="    					{printf("%s\n",yytext); EQ;return RELOP;}
"="    						{printf("%s\n",yytext);return  ASSIGN;}
"+"    						{printf("%s\n",yytext);return  SUM;}
"-"    						{printf("%s\n",yytext);return  SUB;}
"*"    						{printf("%s\n",yytext);return  MUL;}
"/"    						{printf("%s\n",yytext);return  DIV;}
"!="    					{printf("%s\n",yytext);return NE;}
"||"    					{printf("%s\n",yytext);return  OR;}
"&&"    					{printf("%s\n",yytext);return  AND;}
.						{printf("%s\n",yytext);return yytext[0];};
%%
int main()
{
	yylex();
	return 0;
}