import schemdraw
import schemdraw.elements as elem

with schemdraw.Drawing() as d:
     d.config(unit = 2.5)
     d+=elem.Battery().label('Battery', loc='bottom')
     d+=elem.Resistor().right().label('Resistor', loc='bottom')
     d+=elem.Capacitor().down().label('Capacitor', loc='left')
     d+=elem.LED().left().label('LED', loc='bottom')
     d+=elem.lines.Line().up().length(2)
     