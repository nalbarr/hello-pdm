# NA
# - make this a runnable module

def main():
    print('hello from main2')
    # NA
    # - NOTE: not callable but will be invoked on import of package
    # some_script2()
    from hello_pdm import some_script2

if __name__ == '__main__':
    main()