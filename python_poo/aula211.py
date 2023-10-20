# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
class Foo:
    def __init__(self):
        self.public = 'attr public'
        self._protected = 'attr _protected'
        self.__private = 'attr __private'
        print()
        self._protected_method()
        print()
        self.__private_method()
        print()
        
    
    
    def public_method(self):
        print('==============PÚBLIC================')
        print('Atributo público pode ser acessado de qualquer lugar, dentro da classe, das classes filhas ou de outros lugares do projeto.')
        print(f'{self.public=}')
        print('self.public_method = Isso é um método público e pode ser acessado de qualquer lugar.') 
        return 'Fim do public_method'
    
    def _protected_method(self):
        print('==============PROTECTED================')
        print('Atributo protected só pode ser acessado da classe que foi criado ou das classes filhas.')
        print(f'{self._protected=}')
        print('self._protected_method = Isso é um método protegido e só deve ser acessado dentro da classe que está ou classes filhas.')
        return 'Fim do _protected_method'
    
    def __private_method(self):
        print('==============PRIVATE================')
        print('Atributo private só pode ser acessado da classe que foi criado, isso não inclui classes pais e filhas.')
        print(f'{self.__private=}')
        print('self.__private_method = Isso é um método que é privado e deve ser acessado apenas da classe que foi criado')
        return 'Fim do __private_method'
    
c = Foo()
c.public_method()
