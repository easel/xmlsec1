# Makefile for source rpm: xmlsec1
# $Id$
NAME := xmlsec1
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
