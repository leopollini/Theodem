require_relative 'Header'

class Operation < ContentLoader
  def initialize(name, content)
    super name, content

    @returns = @content['returns']
    # @returns ||= {}
    @inherit_types = @content['inherit_types']
    @inherit_types ||= {}
    @requires_proof = @content['requires_proof']
    @requires_proof ||= {}
  end
end
