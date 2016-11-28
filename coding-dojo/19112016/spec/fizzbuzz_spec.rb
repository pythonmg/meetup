require 'spec_helper'
require 'fizzbuzz'

RSpec.describe 'FizzBuzz' do
  it "Se a classe FizzBuzz existe" do
    fizzBuzz = FizzBuzz.new
    expect(fizzBuzz.class == FizzBuzz).to eq true
  end

  it "FizzBuzz de 1 retorna 1" do
      fizzBuzz = FizzBuzz.new
      expect(fizzBuzz.fizz_buzz(1)).to eq [1]
  end

  it "FizzBuzz de 3 retorna 1 2 fizz" do
      fizzBuzz = FizzBuzz.new
      expect(fizzBuzz.fizz_buzz(3)).to eq [1,2,"fizz"]
  end
  it "FizzBuzz de 5 retorna 1 2 fizz 4 buzz" do
      fizzBuzz = FizzBuzz.new
      expect(fizzBuzz.fizz_buzz(5)).to eq [1,2,"fizz",4,"buzz"]
  end
  it "FizzBuzz de 15 retorna array com fizz buzz e fizzbuzz" do
      fizzBuzz = FizzBuzz.new
      arr = fizzBuzz.fizz_buzz(15)
      p arr
      expect(arr.include?("fizzbuzz"))
  end

end
