require_relative 'Header'

# requires: description, type, args, equiv, also
class DefineProperty < ContentLoader
  attr_accessor :name, :args, :equiv, :also

  def getInstance(args)
    Property.new :this, args, @args
  end

  # balls.
  class Property
    attr_accessor :name, :args

    def initialize(prop, args, vars)
      @instanceof = prop
      @args = args
      @argsnames = []
      @args.each_key do |a|
        @argsnames << a
        @args[a] = vars[a]
        puts "assigned #{vars[a]} to #{a}" if DEBUG_MODE
      end
      puts "args names: #{@argsnames}"
    end

    def ==(other)
      @args == other.args
    end

    def expand
      @instanceof.equiv.each do |s| # cycles all equivalent statements
        puts "this lol is equiv to #{s}"
      end
    end
  end
end
