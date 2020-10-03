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
if    {printf("%s\n",yytext); IF;};
while {printf("%s\n",yytext);WHILE;};
for {printf("%s\n",yytext);FOR;};
{digit}+    {printf("%s\n",yytext); NUM;}
{alpha}({alpha}|{digit})*    {printf("%s\n",yytext); ID;}
"<="    {printf("%s\n",yytext); LE;RELOP;}
">="    {printf("%s\n",yytext); GE;RELOP;}
"=="    {printf("%s\n",yytext); EQ;RELOP;}
"="    {printf("%s\n",yytext); ASSIGN;}
"+"    {printf("%s\n",yytext); SUM;}
"-"    {printf("%s\n",yytext); SUB;}
"*"    {printf("%s\n",yytext); MUL;}
"/"    {printf("%s\n",yytext); DIV;}
"!="    {printf("%s\n",yytext); NE;}
"||"    {printf("%s\n",yytext); OR;}
"&&"    {printf("%s\n",yytext); AND;}
.	{printf("%s\n",yytext);yytext[0];};
%%
int main()
{
	yylex();
	return 0;
}
