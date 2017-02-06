#-*- coding:utf-8 -*-#
m_name = 'David'
m_age = 35
m_height = 60
m_weight =170
m_eyes = 'Black'
m_teeth = 'White'
m_hair = 'Black'

print "Let's talk about %s" % m_name
print "He's %d inches tall." % m_height
print "He's %d pounds heavy." % m_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (m_eyes,m_hair)
print "His teeth are usually %s depending on the coffe." % m_teeth
print round(1.733)
# this line is tricky,try to get it exactly right
print "If add %d,%d,and %d I get %d." %(m_age,m_height,m_weight,m_age+m_height+m_weight)