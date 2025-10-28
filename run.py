import sys
import main

if len(sys.argv) > 1:
    main.main()
else:
    print("Usage: python run.py <path/to/obj/file>")
