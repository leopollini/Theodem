require_relative 'assembler/Header'

puts 'Welcome lol'

# begin
#   file = open('lol.json')
# rescue StandardError => e
#   puts e
#   file ||= stdin
# end

Theodem.init open('lol.json')

Theodem.proveTheorem 'loltheorem'
