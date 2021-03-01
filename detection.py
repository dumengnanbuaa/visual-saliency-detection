def visual_saliency_detection(mat):
    fourier = cv2.dft(np.float32(mat), flags=cv2.DFT_COMPLEX_OUTPUT)

    # The square of the real and imaginary parts and then the square root of the real and imaginary parts, resulting in the combined frequency domain for subsequent operations
    # Although the paper mentioned that only the amplitude spectrum was used in the whole calculation and the phase spectrum remained unchanged, the logarithm could not be calculated because the logarithm exceeded the defined domain in the actual calculation of the amplitude spectrum. Moreover, the author of the paper actually calculated the amplitude + phase, so it was consistent with the author's code for the time being
    # Different with paper, the author actually used both imaginary and real part of the frequency domain.
    re, im = cv2.split(fourier)
    base = (re ** 2 + im ** 2) ** 0.5

    # Logarithmic spectrum
    log = cv2.log(base)
    # A smooth curve
    blur = cv2.blur(log, (7, 7))

    # Get residual spectrum of significance
    residual = log - blur

    # Restore the exponential logarithmic spectrum
    residual = cv2.exp(residual)

    # Find the Angle between real and virtual in the original frequency domain, and use the Angle to restore real and virtual
    sin = im / base
    cos = re / base 
    re = residual * cos
    im = residual * sin

    # The inverse Fourier transform
    fourier = cv2.merge((re, im))
    inverse = cv2.dft(fourier, flags=cv2.DFT_INVERSE + cv2.DFT_REAL_OUTPUT)

    # Optimization results display
    min_v, max_v, _, _ = cv2.minMaxLoc(inverse)
    _, thre = cv2.threshold(inverse, 0, 255, cv2.THRESH_TOZERO)
    thre = thre * (255 / max_v)
    res = cv2.GaussianBlur(thre, (7, 7), 0)

    return res