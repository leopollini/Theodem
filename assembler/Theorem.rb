require_relative 'Header'

class Theorem < ContentLoader
  attr_accessor :hypothesis, :thesis, :extract, :procedure

  def initialize(name, content)
    super name, content

    @hypothesis = @content['hypothesis']
    # @hypothesis ||= {}
    @thesis = @content['thesis']
    # @thesis ||= []
    @extract = @content['extract']
    # @extract ||= {}
    @procedure = @content['procedure']
    # @procedure ||= {}
  end
end
