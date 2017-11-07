#!/usr/bin/env python 

import numpy as np 
import matplotlib.pyplot as plt 

def flat_sample(bounds, size=1):

    if bounds[0].shape is not (1,2):
        samples = np.random.uniform(size=size)*(bounds[1]-bounds[0]) + bounds[0]
        return samples 

    samples = np.zeros((size,len(bounds)), dtype=np.float32)    
    for index, dimension in enumerate(bounds):
        samples[:,index] = np.random.uniform(size=size)*(dimension[1]-dimension[0]) + dimension[0]
    return samples

def phase_space_volume(bounds):
    volume = 1.0
    for dimension in bounds:
        volume *= bounds[1]-bounds[0]
    return volume 

def monte_carlo_integrate(pdf, bounds, n_samples):
    samples = flat_sample(bounds, n_samples)
    weights = pdf(samples)
    volume = phase_space_volume(bounds)
    integral = np.sum(weights)*volume/n_samples
    return np.max(weights), integral
    
class BaseSampler(object):
    ''' Interface that defines common 
    sampler behaviour. 
    '''

    def __init__(self):
        pass

    def sample(self, pdf, bounds, n_samples):
        pass

class AcceptRejectSampler(BaseSampler):
    ''' Basic implementation of sampling, 
    where the parameters are generated uniformly over
    the phase space. 
    '''

    def __init__(self):
        pass 


    def sample(self, pdf, bounds, n_samples):
        max, integral = monte_carlo_integrate(pdf, bounds, 10000)
        samples = np.zeros((n_samples,len(bounds)), dtype=np.float32)

        sample_index = 0
        while(sample_index < n_samples):
            x = flat_sample(bounds,size=1)
            weight = pdf(x)/max
            
            print(x)
            print(type(weight))
            print(weight)

            # this is the basic accept reject rule 
            if weight > np.random.uniform(size=1):
                samples[sample_index,:] = x
                sample_index += 1

        return samples



# function for testing 
def gauss(pars, x):
    return pars[0]*np.exp(-0.5*(x-pars[1])**2/pars[2]**2)

def gauss2(pars, x):
    return gauss(pars[:3], x[0])*gauss(pars[3:],x[1])

if __name__ == '__main__':

    sampler = AcceptRejectSampler()
    
#    pars = np.array([1.0, 0.0, 1.0, 1.0, 0.0, 1.0])
#    bounds = np.array([[-1, 1],[-1, 1]])
    pars = np.array([1.0, 0.0, 1.0])    
    bounds = np.array([-3, 3])

    def pdf(x):
        return gauss(pars, x)

    samples = sampler.sample(pdf, bounds, 1000)

    plt.hist(samples, bins=20)
    plt.savefig('samples.pdf', dpi=400)
