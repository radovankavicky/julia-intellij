package org.ice1000.julia.lang.psi

import com.intellij.psi.PsiElement
import com.intellij.util.PsiIconUtil
import icons.JuliaIcons
import org.ice1000.julia.lang.JuliaFile
import org.ice1000.julia.lang.psi.impl.IJuliaFunctionDeclaration
import javax.swing.Icon


val PsiElement.isBlock
	get() = this is JuliaFile ||
		this is JuliaStatements ||
		this is JuliaModuleDeclaration ||
		this is IJuliaFunctionDeclaration ||
		this is JuliaTypeDeclaration ||
		this is JuliaIfExpr ||
		this is JuliaElseIfClause ||
		this is JuliaElseClause ||
		this is JuliaWhileExpr ||
		this is JuliaAssignOp

val PsiElement.canBeNamed
	get() = this is JuliaFile ||
		this is IJuliaFunctionDeclaration ||
		this is JuliaTypeDeclaration ||
		this is JuliaAssignOp ||
		this is JuliaSymbol

val JuliaAssignOp.varOrConstIcon
	get() = if (exprList.firstOrNull()?.let { it.firstChild.node.elementType == JuliaTypes.CONST_KEYWORD } == true)
		JuliaIcons.JULIA_CONST_ICON
	else
		JuliaIcons.JULIA_VARIABLE_ICON

val JuliaIfExpr.compareText
	get() = "if " + statements.exprList.first().text

val JuliaElseIfClause.compareText
	get() = "elseif " + statements.exprList.first().text

val JuliaWhileExpr.compareText
	get() = expr?.text ?: "while"

val JuliaAssignOp.varOrConstName: String
	get() = this.exprList.first().let { if (it is JuliaSymbolLhs) it.symbolList.last().text else it.text }

val IJuliaFunctionDeclaration.functionName:String
	get() = when {
		this is JuliaFunction -> this.symbol?.text.toString()
		this is JuliaCompactFunction -> this.exprList.first().text.toString()
		else -> ""
	}

val IJuliaFunctionDeclaration.typeAndParams:String
	get() = when{
		this is JuliaFunction -> this.typeParameters?.text?:""+this.functionSignature?.text
		this is JuliaCompactFunction -> this.typeParameters?.text?:""+this.functionSignature.text
		else -> ""
	}

val IJuliaFunctionDeclaration.toText:String
	get() = functionName+typeAndParams


fun PsiElement.presentText() = this.let {
	when (it) {
		is JuliaFile -> it.originalFile.name
		is JuliaIfExpr -> it.compareText
		is JuliaElseClause -> "else"
		is JuliaElseIfClause -> it.compareText
		is JuliaAssignOp -> it.varOrConstName
		is JuliaWhileExpr -> it.compareText
		is JuliaTypeDeclaration -> it.exprList.first().text
		is JuliaModuleDeclaration -> it.symbol.text
		is IJuliaFunctionDeclaration -> it.toText
		else -> it.text
	}
}

fun PsiElement.presentIcon(): Icon? {
	return when (this) {
		is JuliaFile -> PsiIconUtil.getProvidersIcon(this, 0)
		is IJuliaFunctionDeclaration -> JuliaIcons.JULIA_FUNCTION_ICON
		is JuliaModuleDeclaration -> JuliaIcons.JULIA_MODULE_ICON
		is JuliaTypeDeclaration -> JuliaIcons.JULIA_TYPE_ICON
		is JuliaWhileExpr -> JuliaIcons.JULIA_WHILE_ICON
		is JuliaAssignOp -> this.varOrConstIcon
		is JuliaIfExpr -> JuliaIcons.JULIA_IF_ICON
		else -> JuliaIcons.JULIA_BIG_ICON
	}
}