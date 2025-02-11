# require 'Header'
require_relative 'Header'

def content_check(content)
  content['theorem'].each do |_theorem, details|
    %w[theorem type hypothesis thesis requres].each do |s|
      return true if details[s].nil?
    end
  end
  false
end

module Theodem
  # attr_accessor :content, :statements, :properties, :theorems, :types, :operations

  def self.init(filestream)
    string = filestream.read
    @content = JSON.parse string.to_s
    @statements = {}
    @properties = {}
    @theorems = {}
    @types = {}
    @operations = {}
    # raise 'Bad content' if DEBUG_MODE && content_check(@content)

    loadStatements
    loadProperites
    loadOperations
    loadTypes
    loadTheorems

    puts 'File read correctly'
  end

  def self.proveTheorem(the_orem)
    raise 'Theorem not found' if @theorems[the_orem].nil?

    Proof.init @theorems[the_orem]
  end

  def self.types
    @types
  end

  def self.theorems
    @theorems
  end

  def self.content
    @content
  end

  def self.properties
    @properties
  end

  def self.operations
    @operations
  end

  def self.statements
    @statements
  end
end
